AI Résumé Critiquer

An interactive Streamlit app that reads a PDF/TXT résumé and asks GPT‑4o‑mini for clear, role‑specific feedback.

Features

Upload a résumé in PDF or TXT format.

Enter a target job title to get tailored suggestions.

Instant, concise feedback on content, skills, and impact.

Secrets stay local – reads OPENAI_API_KEY from a .env file.

Quick Start

# 1. Clone
git clone https://github.com/HarshPahilajani05/resume-critiquer.git
cd resume-critiquer

# 2. (Optional) create a virtual‑env
python -m venv .venv && .venv\Scripts\activate  # Windows
# source .venv/bin/activate                       # macOS / Linux

# 3. Install deps
pip install -r requirements.txt

# 4. Add your key
echo OPENAI_API_KEY=sk-... > .env

# 5. Run the app
streamlit run main.py

Then open http://localhost:8501.

Tech Stack

Python / Streamlit – UI

OpenAI GPT‑4o‑mini – résumé analysis

PyPDF2 – PDF text extraction

python‑dotenv – env‑var management
