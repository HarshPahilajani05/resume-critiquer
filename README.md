# 1. Clone the repo
 git clone https://github.com/HarshPahilajani05/resume-critiquer.git
 cd resume-critiquer

# 2. Create a virtual environment  (optional but recommended)
 python -m venv .venv
 .venv\Scripts\activate            # Windows
# source .venv/bin/activate         # macOS / Linux

# 3. Install dependencies
 pip install -r requirements.txt

# 4. Add your OpenAI key
 # Linux / macOS (current shell only)
 export OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxx"

 # Windows PowerShell (current session only)
 $Env:OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxx"

 # Windows CMD (current session only)
 set OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxx"

# 5. Launch the app
 streamlit run main.py
