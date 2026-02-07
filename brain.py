import os
import requests
from google import genai
from google.genai import types
from utils import build_character_prompt

class CurioBrain:
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)
        self.model_id = "gemini-2.5-flash-preview-09-2025"
        self.image_model = "imagen-4.0-generate-001"
        self.api_key = api_key

    def generate_image(self, prompt):
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.image_model}:predict?key={self.api_key}"
        payload = {
            "instances": [{"prompt": f"A high-quality, professional avatar portrait of {prompt}. Cinematic lighting, detailed, centered."},],
            "parameters": {"sampleCount": 1}
        }
        try:
            response = requests.post(url, json=payload)
            result = response.json()
            if "predictions" in result:
                b64_data = result["predictions"][0]["bytesBase64Encoded"]
                return f"data:image/png;base64,{b64_data}"
        except Exception:
            pass
        return None

    def generate_response(self, query, persona, reasoning, contrast_mode=False, custom_instructions=None):
        if custom_instructions:
            system_instructions = build_character_prompt(persona, custom_instructions)
        else:
            system_instructions = f"You are {persona}. Reasoning Depth: {reasoning}."

        if contrast_mode:
            system_instructions += " Act as a skeptic. Present consensus then provide a counter-perspective."

        search_tool = types.Tool(google_search=types.GoogleSearch())

        try:
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=query,
                config=types.GenerateContentConfig(
                    system_instruction=system_instructions,
                    tools=[search_tool],
                    temperature=0.3 if reasoning == "Deep" else 0.7
                )
            )
            
            sources = []
            if response.candidates[0].grounding_metadata.grounding_chunks:
                for chunk in response.candidates[0].grounding_metadata.grounding_chunks:
                    if chunk.web:
                        sources.append({"title": chunk.web.title, "uri": chunk.web.uri})
            
            return response.text, sources
        except Exception as e:
            return f"Neural link failed: {str(e)}", []