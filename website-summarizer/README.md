# 🌐 Website Summarizer using OpenAI

A simple Python tool that scrapes a website, extracts meaningful text, and generates a **short AI-powered summary** in Markdown format.  

This project demonstrates:
- Web scraping with **BeautifulSoup**
- API integration with **OpenAI GPT models**
- Environment variable handling with **dotenv**
- Command-line interface for flexible usage

---

## 🚀 Features
- Takes any website URL as input
- Cleans out unnecessary HTML elements ('script', 'style', 'img', 'input')
- Extracts title & textual content
- Generates a short **natural language summary** using OpenAI GPT
- Outputs clean Markdown for easy reading

---

## 🛠️ Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/angshudg/website-summarizer.git
cd website-summarizer
pip install -r requirements.txt

Perfect 👍 — here’s a polished **README.md** that you can drop directly into your GitHub repo.
It’s written in recruiter-friendly language so it shows impact + technical depth.

---

### `README.md`

````markdown
# 🌐 Website Summarizer using OpenAI

A simple Python tool that scrapes a website, extracts meaningful text, and generates a **short AI-powered summary** in Markdown format.  

This project demonstrates:
- Web scraping with **BeautifulSoup**
- API integration with **OpenAI GPT models**
- Environment variable handling with **dotenv**
- Command-line interface for flexible usage

---

## 🚀 Features
- Takes any website URL as input
- Cleans out unnecessary HTML elements (`script`, `style`, `img`, etc.)
- Extracts title & textual content
- Generates a short **natural language summary** using OpenAI GPT
- Outputs clean Markdown for easy reading

---

## 🛠️ Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/<your-username>/website-summarizer.git
cd website-summarizer
pip install -r requirements.txt
````

---

## 🔑 Setup

1. Create a `.env` file in the project root:

   ```bash
   echo "OPENAI_API_KEY=sk-proj-xxxxxxx" > .env
   ```

   Replace `sk-proj-xxxxxxx` with your actual OpenAI API key.

2. Verify that dependencies are installed:

   ```bash
   pip list
   ```

---

## ▶️ Usage

Run the script with a website URL:

```bash
python summarize_website.py https://<provide-url-here>/
```

---

## 📂 Project Structure

```
.
├── summarize_website.py   # Main script with CLI
├── requirements.txt       # Dependencies
├── .env                   # API key (not committed to Git)
└── README.md              # Documentation
```

---

## 📌 Example Use Cases

* Summarize **news sites** into quick bullet points
* Extract **announcements** from corporate pages
* Turn **blogs** into concise overviews
* Crawl research portals for **study notes**

---

## ⚡ Tech Stack

* **Python 3.9+**
* **Requests** (HTTP requests)
* **BeautifulSoup** (web scraping)
* **dotenv** (environment variables)
* **OpenAI API** (text summarization)

```
