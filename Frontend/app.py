import streamlit as st
import requests

st.set_page_config(page_title="Text Summarization", layout="centered")
st.title("📝 Summarizer")

st.markdown("Enter a long piece of text below. The app will summarize it using a local model running on a FastAPI backend.")

# Input box
text_input = st.text_area("✍️ Enter your long text here:", height=300)

# Button
if st.button("Generate Summary"):
    if not text_input.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("⏳ Generating summary..."):
            try:
                response = requests.post("http://localhost:8000/summarize/", json={"text": text_input})
                if response.status_code == 200:
                    summary = response.json()["summary"]
                    st.success("✅ Summary:")
                    st.write(summary)
                else:
                    st.error(f"Server error: {response.status_code}")
            except Exception as e:
                st.error(f"❌ Could not connect to backend.\nError: {e}")
