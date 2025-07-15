# LLM_SUMMARIZER
End-to-end LLM-powered text summarization app with FastAPI backend, Streamlit frontend, and local HuggingFace model integration.

A modular AI application for generating concise summaries from long texts using state-of-the-art Large Language Models (LLMs).  
The project features a FastAPI backend for serving the model, a Streamlit frontend for user interaction, and supports easy model management with local HuggingFace integration.

- 🔄 FastAPI backend for robust, scalable API
- 📝 Streamlit frontend for user-friendly input/output
- 🤗 Model loading from local directory (downloaded via script).
- - This project uses the `google/flan-t5-base` model from Hugging Face for summarization (but can be swapped in any compatible model)
    
## 🚀 Getting Started

1️⃣ Clone the repo
```bash
git clone https://github.com/Afsana0304/LLM_SUMMARIZER.git
cd LLM_SUMMARIZER
```

2️⃣ Install dependencies
```bash
python -m venv venv
source venv/bin/activate(Mac)     # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
3️⃣ Download the model
```bash
cd models
python download_model.py    
Note: The repo_id in download_model.py can be changed to use any summarization model from Hugging Face.
```

4️⃣ Run the backend (FastAPI)
```bash
cd Backend
uvicorn app.main:app --reload
```

5️⃣ Run the frontend (Streamlit)
```bash
Open a new terminal(make sure to use the same environemnt as backend):
cd Frontend
streamlit run app.py
```

🔖 Notes
🗂️ Model files are gitignored—use models/download_model.py to fetch them.


## 🎬 Demo
demo.mov


