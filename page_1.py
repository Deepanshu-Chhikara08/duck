import streamlit as st
from transformers import pipeline
from huggingface_hub import login
import torch
import os

# Free up GPU memory
torch.cuda.empty_cache()

# Set environment variable to avoid fragmentation
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"

access_token_read = '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'
login(token = access_token_read)

device = 0 if torch.cuda.is_available() else -1
pipe = pipeline("text-generation", model="HuggingFaceTB/SmolLM2-1.7B-Instruct", device=-1)

st.title("Text GenAI Model")
text = st.text_input("Enter Your Prompt")
messages = [
    {"role": "user"},
]
messages[0]["content"] = text

gentext = pipe(messages, max_new_tokens=100)
st.write(gentext)[1]["content"]