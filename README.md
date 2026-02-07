Curio: Neural Sandbox

Curio is a modular AI reasoning environment powered by the Gemini 3 API. It is designed to move beyond traditional "helpful assistant" paradigms by providing a sandbox for stress-testing information through live search grounding and multimodal persona synthesis.

Project Overview

Curio provides a dual-interface for interacting with LLMs:

Neural Sandbox: A high-fidelity research environment grounded in real-time Google Search data.

Character Forge: A multimodal tool that combines Imagen 4.0 with Gemini 3 to create persistent, lore-accurate AI entities.

The core innovation of the project is Contrast Mode, which utilizes Gemini's reasoning capabilities to act as an intellectual skeptic, challenging user assumptions and identifying logical fallacies in real-time.

Core Features

1. Character Forge

The Forge allows users to instantiate specific "AI Souls."

Visual Synthesis: Uses Imagen 4.0 to generate cinematic avatar portraits based on character descriptions.

Persona Maintenance: Leverages Gemini 3's sophisticated instruction following to ensure characters maintain consistent vocabulary, tone, and logical frameworks.

2. Contrast Mode & Reasoning Depth

Users can control the intensity of the AI's skepticism through a "Reasoning Depth" selector:

Surface: Quick, direct responses.

Standard: Balanced reasoning.

Deep: Comprehensive chain-of-thought analysis.

When Contrast Mode is active, the system prompt is reconfigured to prioritize counter-perspectives. The model's "Focus Level" (Temperature) is tightened to approximately 0.2 to ensure high logical consistency, mathematically nudging the output toward the antithesis of the user's initial query.

3. Native Grounding

Curio bypasses traditional Retrieval-Augmented Generation (RAG) by using Gemini 3's native Google Search grounding. This ensures that responses are synthesized from live, cited web sources without the latency of external vector databases.

Technical Stack

Language: Python 3.9+

Frontend: Streamlit

API Models: Gemini 3 (2.5 Flash Preview), Imagen 4.0

Database: SQLite (local persistence for interaction logs)

Libraries: google-genai, python-dotenv, requests

Repository Structure

main.py: The primary UI and state management layer.

brain.py: Orchestration of Gemini 3 reasoning, grounding, and Imagen 4.0 generation.

utils.py: Database operations, persistent logging, and character prompt engineering.

requirements.txt: System dependencies.

curio_memory.db: Local SQLite database (created on first run).

Installation

Clone the repository:

git clone [https://github.com/Rishika-1212/curio-neural-sandbox.git](https://github.com/Rishika-1212/curio-neural-sandbox.git)
cd curio-neural-sandbox


Install dependencies:

pip install -r requirements.txt


Configure API Secrets:
Create a .env file in the root directory or configure your environment variables:

GEMINI_API_KEY=your_google_ai_studio_key


Launch the Sandbox:

streamlit run main.py


Security Note

This project uses a .gitignore to prevent the upload of .env files and local curio_memory.db files. Ensure your API keys are managed through Streamlit Secrets or Environment Variables when deploying to the cloud.

Developed for the Gemini 3 API Competition.
