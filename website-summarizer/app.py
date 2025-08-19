import os
import requests
import streamlit as st
from bs4 import BeautifulSoup
from openai import OpenAI

HF_API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

# ---------------- Core Classes & Functions ----------------
class Website:
    def __init__(self, url: str):
        self.url = url
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        self.text = soup.body.get_text(separator="\n", strip=True)

def summarize_openai(api_key, url):
    openai = OpenAI(api_key=api_key)
    website = Website(url)
    messages = [
        {"role": "system", "content": "Summarize the website in markdown"},
        {"role": "user", "content": website.text},
    ]
    response = openai.chat.completions.create(
        model="gpt-5-nano",
        messages=messages,
    )
    return response.choices[0].message.content

def summarize_hface(hf_token, url):
    website = Website(url)
    content = f"Title: {website.title}\n\n{website.text}"
    headers = {"Authorization": f"Bearer {hf_token}"}
    payload = {"inputs": content, "parameters": {"min_length": 40, "max_length": 200}}
    response = requests.post(HF_API_URL, headers=headers, json=payload, timeout=60)

    if response.status_code != 200:
        return f"Hugging Face API Error {response.status_code}: {response.text}"

    result = response.json()
    if isinstance(result, list) and "summary_text" in result[0]:
        return result[0]["summary_text"]
    return "Could not generate summary."

# ---------------- UI -----------------
st.set_page_config(page_title="Website Summarizer", layout="wide")
st.title("🌐 Website Summarizer Tool")

# Sidebar: API keys
st.sidebar.header("API Tokens")
openai_key = st.sidebar.text_input("OpenAI API Key", type="password")
hf_key = st.sidebar.text_input("HuggingFace API Key", type="password")

# Center: Inputs
url = st.text_input("Enter website URL:")
model = st.selectbox("Choose summarization model:", ["OpenAI", "HuggingFace"])

if st.button("Submit"):
    if not url:
        st.error("Please enter a website URL.")
    elif model == "OpenAI":
        if not openai_key:
            st.error("Please enter OpenAI API key in sidebar.")
        else:
            with st.spinner("Summarizing with OpenAI..."):
                summary = summarize_openai(openai_key, url)
                st.markdown("### OpenAI Summary")
                st.markdown(summary)
    else:
        if not hf_key:
            st.error("Please enter Hugging Face API key in sidebar.")
        else:
            with st.spinner("Summarizing with Hugging Face..."):
                summary = summarize_hface(hf_key, url)
                st.markdown("### Hugging Face Summary")
                st.markdown(summary)
