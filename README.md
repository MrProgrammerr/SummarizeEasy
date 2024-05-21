# SummarizeEasy
 
This repository contains a Streamlit application that allows users to summarize text either by entering it directly or by uploading a PDF file. The app utilizes the langchain library and a pre-trained LLaMA model to generate concise summaries in bullet points.

## Features
<ul>
<li>Enter text directly into a text area.</li>
<li>Upload a PDF file to extract and summarize its text content.</li>
<li>View the extracted text from the uploaded PDF.</li>
<li>Get a bullet-point summary of the text.</li>
</ul>

## How It Works
<ol>
<li>Text Input: Users can input text manually or upload a PDF file.</li>
<li>Text Extraction: If a PDF is uploaded, the text is extracted using PyPDF2.</li>
<li>Text Segmentation: The text is split into manageable segments to ensure effective summarization.</li>
<li>Prompt Generation: Each text segment is formatted into a prompt using a predefined template.</li>
<li>Summarization: The LLaMA model generates a summary for each text segment.</li>
<li>Summary Display: The generated summaries are combined and displayed in the app.</li>
</ol>