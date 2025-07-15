import os
from transformers import  AutoTokenizer, AutoModelForSeq2SeqLM

# Load the model from the local directory.
# Note: Run models/download_model.py beforehand to ensure the model is downloaded.

root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
model_path = os.path.join(root, "models", "flan-t5-base-local")

tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True)
model = AutoModelForSeq2SeqLM.from_pretrained(model_path, local_files_only=True)


def generate_summary(text: str) -> str:
    """
    Generates summary using FLAN-T5 model.
    """
    
    # Use the T5/FLAN prompt style for summarization
    prompt = f"Act as a summarization expert. Summarize the following text in a clear and concise manner: {text}"
    
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids

    # Generate output 
    outputs = model.generate(
        input_ids,
        max_length=200,  # Adjust for shorter/longer summaries 
        min_length=30,   # Adjust for shorter/longer summaries 
        do_sample=False,
        num_beams= 3,
        num_return_sequences=1,
        early_stopping=True
    )
    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return summary.strip()
    
    
