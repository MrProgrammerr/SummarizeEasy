import streamlit as st
from PyPDF2 import PdfReader
import io
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers

# Initialize the model with the specified configuration
llm = CTransformers(model='llama-2-7b-chat.ggmlv3.q8_0.bin',
                    model_type='llama',
                    config={'max_new_tokens': 256,
                            'temperature': 0.01})

# Define the template for the summarization prompt
template = """
Write a concise summary of the following text delimited by triple backquotes.
Return your response in bullet points which covers the key points of the text.
```{text}```
BULLET POINT SUMMARY:
"""

# Create a PromptTemplate object with the specified template and input variables
prompt = PromptTemplate(template=template, input_variables=["text"])

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def split_text_into_segments(text, max_segment_length=512):
    tokens = text.split()
    segments = []
    current_segment = []
    current_length = 0

    for token in tokens:
        token_length = len(token) + 1  # Add 1 for the space
        if current_length + token_length > max_segment_length:
            segments.append(' '.join(current_segment))
            current_segment = [token]
            current_length = token_length
        else:
            current_segment.append(token)
            current_length += token_length

    if current_segment:
        segments.append(' '.join(current_segment))

    return segments

# Streamlit app interface
st.title("Text Summarization App")

# Option to enter text or upload PDF
input_text = st.text_area("Enter Text:", height=200)
uploaded_file = st.file_uploader("Or upload a PDF file", type=["pdf"])

# Extract text from the uploaded PDF
if uploaded_file is not None:
    input_text = extract_text_from_pdf(uploaded_file)
    st.text_area("Extracted Text from PDF:", input_text, height=200)

# Generate summary if there is any input text
if input_text:
    # Split text into segments
    text_segments = split_text_into_segments(input_text)
    
    # Generate summary for each segment
    summarized_segments = []
    for segment in text_segments:
        # Format the prompt with the segment
        formatted_prompt = prompt.format(text=segment)

        # Generate the response from the LLaMA model using the formatted prompt
        response = llm(formatted_prompt).strip()
        if response:
            summarized_segments.append(response)
    
    # Combine summarized segments into a single summary
    summarized_text = "\n\n".join(summarized_segments)
    
    # Display the generated summary
    st.text_area("Summary:", summarized_text, height=200)
