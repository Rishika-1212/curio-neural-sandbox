import os
import requests
import base64
from google import genai
from google.genai import types

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

    def generate_response(self, query, persona, depth, contrast_mode=False, custom_instructions=None):
        system_instructions = f"You are {persona}. Depth: {depth}."
        
        if custom_instructions:
            system_instructions = f"Act as this specific character: {custom_instructions}. Never break character. Use their vocabulary and style."

        if contrast_mode:
            system_instructions += " Additionally, act as a skeptic and provide counter-perspectives."

        search_tool = types.Tool(google_search=types.GoogleSearch())

        try:
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=query,
                config=types.GenerateContentConfig(
                    system_instruction=system_instructions,
                    tools=[search_tool],
                    temperature=0.8
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