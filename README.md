# AI Résumé Critiquer

Quick, copy-paste setup to run the Streamlit app.

```bash
# 1 Clone the repo
git clone https://github.com/HarshPahilajani05/resume-critiquer.git
cd resume-critiquer

# 2 (Recommended) create a virtual env
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS / Linux

# 3 Install dependencies
pip install -r requirements.txt

# 4 Add your OpenAI key
# Linux / macOS (current shell)
export OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxx"
# Windows PowerShell (current session)
$Env:OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxx"
# Windows CMD (current session)
set OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxx"

# 5 Launch the app
streamlit run main.py
