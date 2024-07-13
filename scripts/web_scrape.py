# Web scraping script
import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape_who_tobacco():
    url = "https://www.who.int/news-room/fact-sheets/detail/tobacco"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    content_div = soup.find('div', id="PageContent_T0643CD2A003_Col00")

    data = []

    if content_div:
        sections = content_div.find_all(['h2', 'h3'])
        for section in sections:
            section_text = section.get_text(strip=True)
            next_sibling = section.find_next_sibling(['p', 'ul'])
            while next_sibling and next_sibling.name in ['p', 'ul']:
                if next_sibling.name == 'p':
                    data.append((section_text, next_sibling.get_text(strip=True)))
                elif next_sibling.name == 'ul':
                    for li in next_sibling.find_all('li'):
                        data.append((section_text, li.get_text(strip=True)))
                next_sibling = next_sibling.find_next_sibling(['p', 'ul'])

        df_who = pd.DataFrame(data, columns=['Section', 'Information'])
        df_who.to_csv('../data/who_tobacco_data.csv', index=False)


scrape_who_tobacco()