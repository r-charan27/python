import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl.workbook import Workbook

# Function to scrape data from the website
def scrape_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the relevant data in the HTML
    # Modify this section based on the structure of the website
    data = []
    table = soup.find('table')
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
           
    return data

# Function to save data to an Excel file
def save_to_excel(data, filename):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False, header=False)

if __name__ == "__main__":
    # URL of the website to scrape
    url = 'https://byjus.com/govt-exams/country-capital-currency/'
    
    # Scrape data
    scraped_data = scrape_data(url)
    
    # Save data to Excel file
    save_to_excel(scraped_data, 'D:/python DE/scraped_data.xlsx')
