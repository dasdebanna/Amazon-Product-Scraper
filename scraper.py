import requests
from bs4 import BeautifulSoup
import csv

def scrape_product_listings(url, num_pages):
    products = []
    
    for page in range(1, num_pages + 1):
        page_url = url + '&page=' + str(page)
        response = requests.get(page_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        listings = soup.find_all('div', {'data-component-type': 's-search-result'})
        
        for listing in listings:
            product = {}
            
            product['Product URL'] = 'https://www.amazon.in' + listing.find('a', {'class': 'a-link-normal s-no-outline'}).get('href')
            product['Product Name'] = listing.find('span', {'class': 'a-size-medium a-color-base a-text-normal'}).text.strip()
           
            price_element = listing.find('span', {'class': 'a-offscreen'})
            product['Product Price'] = price_element.text.strip() if price_element else 'N/A'
            
            product['Rating'] = listing.find('span', {'class': 'a-icon-alt'}).text.strip().split()[0]
            product['Number of reviews'] = listing.find('span', {'class': 'a-size-base'}).text.strip().replace(',', '')
            
            products.append(product)
    
    return products

def scrape_product_details(products):
    for product in products:
        url = product['Product URL']
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        description_element = soup.find('div', {'id': 'productDescription'})
        product['Description'] = description_element.get_text(strip=True) if description_element else 'N/A'
        
        asin_element = soup.find('th', {'class': 'a-color-secondary a-size-base prodDetAttrValue'})
        asin_value = asin_element.find_next_sibling('td').get_text(strip=True) if asin_element else 'N/A'
        product['ASIN'] = asin_value if asin_value and asin_value != 'ASIN' else 'N/A'
        
        product['Product Description'] = description_element.get_text(strip=True) if description_element else 'N/A'
        
        manufacturer_element = soup.find('a', {'id': 'bylineInfo'})
        product['Manufacturer'] = manufacturer_element.get_text(strip=True) if manufacturer_element else 'N/A'

        
if __name__ == '__main__':
  
    url = 'https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_'
    num_pages = 20
    
    products = scrape_product_listings(url, num_pages)
    
    scrape_product_details(products)
    

    keys = products[0].keys()
    with open('product_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        writer.writerows(products)
