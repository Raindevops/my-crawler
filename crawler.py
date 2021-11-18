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
    
def start_crawling(soup, filename):
    extract_products(soup, filename)
    # pagination = soup.find('ul',{'class': 'pagination-custom'})
    # next_page = pagination.find_all('li')[-1]
    # if next_page.has_attr('class'):
    #     if next_page['class'] == ['disabled']:
    #         print("You reached the last page, stopping crawler...")
    # else:
    #     next_page_link = next_page.find('a')['href']
    #     next_page_address = BASE_URL + next_page_link
    #     next_page_index = next_page_link[next_page_link.find('=') + 1 ]
    #     crawl(next_page_address, f'etee-page{next_page_index}.txt')

def extract_products(soup, filename):
    csv_filename = filename.replace('.txt','.csv')
    products_file = open(f'products/{csv_filename}', mode='a', encoding='utf-8', newline='')
    products_writer = csv.writer(products_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    products_writer.writerow(['Band', 'Album', 'Year'])
    products = soup.find_all('table', {'class': 'table table-compact table-striped'})[0].find('tbody')


    for product in products:
        base = product.find('td',{'class':'', 'width':'', 'align':''})
        band = base.find('b').find('a').getText()
        albums = base.find('div',{'class':'visible-xs'}).find('a').getText()
        years = base.find('div',{'class':'visible-xs'}).find('span').getText()

def crawl(url, filename):
    page_body = get_page_source(url, filename)
    soup = BeautifulSoup(page_body, 'html.parser')
    start_crawling(soup, filename)

crawl(FULL_START_URL,'etee-page1.txt')

