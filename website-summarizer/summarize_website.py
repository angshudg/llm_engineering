import os
import sys
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from openai import OpenAI

# Load environment variables
load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    print("❌ No API key found! Please set OPENAI_API_KEY in your .env file.")
    sys.exit(1)
elif not api_key.startswith("sk-proj-") or api_key.strip() != api_key:
    print("❌ API key corrupted. Please check formatting.")
    sys.exit(1)
else:
    print("✅ API key loaded successfully.")
    openai = OpenAI()

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/117.0.0.0 Safari/537.36"
    )
}

class Website:
    def __init__(self, url: str):
        """
        Create this Website object from the given URL using BeautifulSoup.
        """
        self.url = url
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        self.text = soup.body.get_text(separator="\n", strip=True)

system_prompt = (
    "You are an assistant that analyzes the contents of a website "
    "and provides a short summary, ignoring text that might be navigation related. "
    "Respond in markdown."
)

def user_prompt_for(website: Website) -> str:
    return (
        f"You are looking at a website titled {website.title}\n\n"
        "The contents of this website are as follows; "
        "please provide a short summary of this website in markdown. "
        "If it includes news or announcements, then summarize these too.\n\n"
        f"{website.text}"
    )

def messages_for(website: Website):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_for(website)},
    ]

def summarize(url: str) -> str:
    website = Website(url)
    response = openai.chat.completions.create(
        model="gpt-5-nano",
        messages=messages_for(website),
    )
    return response.choices[0].message.content

def main():
    if len(sys.argv) != 2:
        print("Usage: python summarize_website.py <website_url>")
        sys.exit(1)

    url = sys.argv[1]
    try:
        summary = summarize(url)
        print("\n=== Website Summary ===\n")
        print(summary)
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
