from langchain.tools import tool
from dotenv import load_dotenv
load_dotenv()
from rich import print
import requests
from bs4 import BeautifulSoup
import os

@tool
def scrape_webpage(url: str) -> str:
    """
    Scrape the content of a webpage from the given URL using Beautiful Soup.
    Returns the cleaned text content of the page.
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'lxml')
        for tag in soup(['header', 'footer', 'nav', 'aside']):
            tag.decompose()
        
        text = soup.get_text()
        
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        
        return text[:3000] 
    except Exception as e:
        return f"Error scraping {url}: {str(e)}"


