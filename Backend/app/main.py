from fastapi import FastAPI
from pydantic import BaseModel
from app.summarizer import generate_summary 
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow Streamlit to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input data model
class InputText(BaseModel):
    text: str

# POST endpoint to summarize text
@app.post("/summarize/")
def summarize(input_text: InputText):
    summary = generate_summary(input_text.text)
    return {"summary": summary}
