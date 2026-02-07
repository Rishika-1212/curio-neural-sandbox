🧠 Curio: Neural Sandbox

Don't just search the web. Spar with it.

Curio is a modular AI reasoning environment powered by the Gemini 3 API. It is designed to move beyond traditional "helpful assistant" paradigms by providing a sandbox for stress-testing information through live search grounding and multimodal persona synthesis.

<img width="1919" height="864" alt="image" src="https://github.com/user-attachments/assets/0d00f0cd-f64f-48c8-90de-a1cedeb912be" />


🚀 The Core Philosophy

Traditional AI assistants are programmed to be agreeable "yes-men." Curio breaks that cycle. By leveraging Gemini 3’s Deep Reasoning, Curio acts as an intellectual sparring partner, forcing users to defend their logic against a grounded, well-researched skeptic.

🛠 Key Technical Features

🎭 The Character Forge

[ Multimodal Synthesis ] [ Imagen 4.0 ] Forge a persistent "AI Soul" with a cinematic identity.

Visual Identity: Generates high-fidelity avatar portraits using Imagen 4.0.

Persona Maintenance: Uses advanced instruction following to ensure entities (like Tony Stark or Socrates) maintain consistent vocabulary and style without breaking character.

<img width="1919" height="861" alt="image" src="https://github.com/user-attachments/assets/34df5a9d-32e8-45df-ad46-d65388acecfa" />


🥊 Contrast Mode

[ Reasoning Depth ] [ Chain-of-Thought ] A toggle that transforms the assistant into a rigorous skeptic.

Logic: Mathematically targets the "antithesis" of user queries to break confirmation bias.

Precision: Tightens the model's "Focus Level" (Temperature) to ~0.2 for hyper-logical, low-hallucination responses.

<img width="1919" height="854" alt="image" src="https://github.com/user-attachments/assets/dfe668d3-6f76-4481-a789-19a93660ca78" />


🌐 Native Grounding

[ Real-Time Data ] [ Zero-Latency RAG ] Bypasses manual RAG pipelines by using Gemini 3's native Google Search tools.

Live Verification: Synthesizes information from current web sources with citations.

Contextual Accuracy: Ensures even obscure or brand-new topics are answered with factual precision.

<img width="1918" height="862" alt="image" src="https://github.com/user-attachments/assets/89779d55-b6c1-40b8-b1cf-1ee878ad6bc2" />


🧪 The "Sandbox" Logic

To ensure the sparring is rigorous, Curio modulates how the AI chooses its words based on your Reasoning Depth setting:

The Probability Calculation:
Probability Score = (Word Score / Focus Level) / (Sum of all Word Scores)

In Deep Reasoning mode, the "Focus Level" (Temperature) is minimized. Curio then nudges the model to select the word most similar to "NOT [Your Query]", forcing a counter-perspective that is still logically sound and grounded in fact.

🏗 Repository Structure

main.py - Primary UI and Session State management.

brain.py - Orchestration of Gemini 3 reasoning, grounding, and Imagen 4.0.

utils.py - SQLite persistence, logging, and persona engineering.

requirements.txt - System dependencies.

curio_memory.db - Local interaction logs (auto-generated).

⚡ Quick Start

1. Clone & Install

git clone [https://github.com/Rishika-1212/curio-neural-sandbox.git](https://github.com/Rishika-1212/curio-neural-sandbox.git)
cd curio-neural-sandbox
pip install -r requirements.txt


2. Configure Secrets

Create a .env file or set your environment variable:

GEMINI_API_KEY=your_google_ai_studio_key


3. Launch

streamlit run main.py


🔒 Security & Deployment

This project is built with security-first principles:

Secrets: Configured for st.secrets compatibility on Streamlit Cloud.

Ignore List: Pre-configured .gitignore prevents leaks of .env or local .db files.

Developed for the Gemini 3 API Competition
