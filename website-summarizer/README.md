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
