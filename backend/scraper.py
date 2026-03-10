import requests
from bs4 import BeautifulSoup

def clean_text(text):
    """Clean the text and try to ignore the other jargon on the website"""
    lines = text.split("\n")
    # Keep only lines with meaningful content
    cleaned = [line.strip() for line in lines if len(line.strip()) > 40]
    return "\n".join(cleaned)

def scrape_job_desc(url):
    """Scrape the actual website by fetching the HTML"""
    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')
        
    else:
        print(f"Error: {response.status_code}")

    return clean_text(soup.get_text())

