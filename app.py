pip install streamlit transformers
import streamlit as st
from transformers import pipeline

# Load the summarization model
summarizer = pipeline("summarization")

# Set the title of the app
st.title("Text Summarizer App")
st.title("Developed by HUma")
# Create a text area for user input
input_text = st.text_area("Enter text to summarize:", height=300)

# Button to trigger summarization
if st.button("Summarize"):
    if input_text:
        # Generate the summary
        summary = summarizer(input_text, max_length=130, min_length=30, do_sample=False)
        st.subheader("Summary:")
        st.write(summary[0]['summary_text'])
    else:
        st.error("Please enter some text to summarize.")
streamlit run summarizer_app.py
