# LLM_SUMMARIZER
End-to-end LLM-powered text summarization app with FastAPI backend, Streamlit frontend, and local HuggingFace model integration.

A modular AI application for generating concise summaries from long texts using state-of-the-art Large Language Models (LLMs).  
The project features a FastAPI backend for serving the model, a Streamlit frontend for user interaction, and supports easy model management with local HuggingFace integration.

- 🔄 FastAPI backend for robust, scalable API
- 📝 Streamlit frontend for user-friendly input/output
- 🤗 Model loading from local directory (downloaded via script)

## 🚀 Getting Started

1️⃣ Clone the repo

git clone https://github.com/Afsana0304/LLM_SUMMARIZER.git
cd LLM_SUMMARIZER 

2️⃣ Install dependencies

python -m venv venv
source venv/bin/activate(Mac)     # On Windows: venv\Scripts\activate
pip install -r requirements.txt

3️⃣ Download the model
cd models
python download_model.py

4️⃣ Run the backend (FastAPI)
cd Backend
uvicorn app.main:app --reload

5️⃣ Run the frontend (Streamlit)
Open a new terminal:
cd Frontend
streamlit run app.py

🔖 Notes
🗂️ Model files are gitignored—use models/download_model.py to fetch them.





