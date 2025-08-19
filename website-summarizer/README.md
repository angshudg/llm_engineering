# Website Summarizer Tool

This project provides a simple web app to summarize any website using **OpenAI** or **Hugging Face** models. The app is built with **Streamlit** and can be run locally or deployed on **Streamlit Cloud**.
<img width="1919" height="991" alt="image" src="https://github.com/user-attachments/assets/ebc25d92-6343-4803-af82-3cba2dd0fe19" />

## Features
- Enter your own API keys (OpenAI or Hugging Face) securely in the sidebar.
- Input a website URL.
- Choose the summarization backend:
  - OpenAI (`gpt-5-nano`)
  - Hugging Face (`facebook/bart-large-cnn`)
- Get a clean summary in markdown format.

## Running Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/angshudg/llm_engineering.git
   cd llm_engineering/website-summarizer
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Start the Streamlit app:

   ```bash
   streamlit run app.py
   ```

4. Open the URL shown in the terminal (usually `http://localhost:8501`) in your browser.

5. Enter your API keys in the sidebar, provide a website URL, choose the model, and click Submit to generate a summary.

## Deploying on Streamlit Cloud

1. Push your code to a GitHub repository.

   Example repo structure:

   ```
   llm_engineering/
   ├── website-summarizer/
   │   ├── app.py
   │   ├── requirements.txt
   │   └── README.md
   ```

2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud) and log in with your GitHub account.

3. Click "New app" and fill in the fields:

   * **Repository:** `your-username/llm_engineering`
   * **Branch:** `main`
   * **Main file path:** `website-summarizer/app.py`

4. Deploy the app. Streamlit will build it automatically and provide a public URL.

5. Open the app in your browser, enter your API keys, and start summarizing websites.

## Notes

* Each user must provide their own API keys through the sidebar. They are not stored in the app.
* Streamlit Cloud free accounts have limits (around 1 GB RAM, 1 GB storage, and 3 apps per account). This app runs well within those limits.
* For production use or persistent API keys, Streamlit Secrets Manager can be configured, but for this project, users are expected to enter their own keys.
