import os
import requests
from bs4 import BeautifulSoup

username = os.getenv("GLASSDOOR_USER")
password = os.getenv("GLASSDOOR_PASS")

def login_and_scrape():
    print("[🔐] Logging into Glassdoor...")
    session = requests.Session()

    login_url = "https://www.glassdoor.co.in/profile/login_input.htm"
    response = session.get(login_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    payload = {
        'username': username,
        'password': password,
        'rememberMe': 'true'
    }

    print("[🌐] Submitting login form...")
    login_response = session.post(login_url, data=payload)

    if "Sign Out" in login_response.text:
        print("[✅] Login successful!")
    else:
        print("[❌] Login may have failed – check credentials or CAPTCHA")

    sample_url = "https://www.glassdoor.co.in/Interview/Google-Interview-Questions-E9079.htm"
    html = session.get(sample_url).text
    soup = BeautifulSoup(html, 'html.parser')

    print("[🔎] Scraping questions...")
    questions = soup.find_all("span", {"class": "interviewQuestion"})

    os.makedirs("data", exist_ok=True)
    with open("data/questions.txt", "w", encoding="utf-8") as f:
        for q in questions:
            f.write(q.text.strip() + "\n")

    print(f"[✅] Saved {len(questions)} questions to data/questions.txt")

if __name__ == "__main__":
    login_and_scrape()
