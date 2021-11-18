import requests
from bs4 import BeautifulSoup
import csv
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://metalstorm.net"
SECTION = "/bands/albums_top.php"
FULL_START_URL = BASE_URL + SECTION
API_KEY = os.getenv('API_KEY')

ENDPOINT = "https://api.webscrapingapi.com/v1/"

def get_page_source(url, filename):
    params = {
        "api_key": API_KEY,
        "url": url,
        "render_js": '1'
    }
    page = requests.request("GET",ENDPOINT, params = params)
    soup = BeautifulSoup(page.content,'html.parser')
    body = soup.find('body')
    file_source = open(filename, mode='w', encoding='utf-8')
    file_source.write(str(body))
    file_source.close()
    return str(body)
    

def extract_top_200(soup, filename):
    csv_filename = filename.replace('.txt','.csv')
    top_200 = open(f'musics/metal/{csv_filename}', mode='a', encoding='utf-8', newline='')
    top_writer = csv.writer(top_200, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    top_writer.writerow(['Band', 'Album', 'Year'])
    tops = soup.find_all('table', {'class': 'table table-compact table-striped'})[0].find('tbody')

    for top in tops:
        base = top.find('td',{'class':'', 'width':'', 'align':''})
        band = base.find('b').find('a').getText()
        albums = base.find('div',{'class':'visible-xs'}).find('a').getText()
        years = base.find('div',{'class':'visible-xs'}).find('span').getText()
        top_writer.writerow([band,albums,years])

def crawl(url, filename):
    page_body = get_page_source(url, filename)
    soup = BeautifulSoup(page_body, 'html.parser')
    extract_top_200(soup, filename)

crawl(FULL_START_URL,'crawl-top-200.txt')

