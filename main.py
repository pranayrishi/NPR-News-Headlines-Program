import requests
from bs4 import BeautifulSoup


def scrape_headlines():
    url = "https://www.npr.org/sections/news/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        headlines = soup.find_all('h2', class_='title')

        print("\n---NPR News Headlines---")
        for i, headline in enumerate(headlines[:10], start=1):
            print(f"{i}. {headline.get_text(strip=True)}")
    else:
        print(f"Failed to retreive the page. Status code: {response.status_code}")

if __name__ == "__main__":
    scrape_headlines()
