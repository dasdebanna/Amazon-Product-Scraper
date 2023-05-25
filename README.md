
Amazon Product Scraper

This project is a Python-based web scraper that extracts product listings and details from Amazon.in. It utilizes the requests library for making HTTP requests and BeautifulSoup library for parsing HTML content.

The scraper allows you to specify the search query and the number of pages to scrape. It retrieves information such as product name, URL, price, rating, number of reviews, description, ASIN, product description, and manufacturer. The extracted data is then exported to a CSV file for further analysis and processing.


## Tech Stack

Python 3.11.3; requests library; BeautifulSoup library


## Installation

1. Clone the repository:

```bash
  git clone https://github.com/your-username/amazon-product-scraper.git
```
2. Install the required libraries using pip:
```bash
  pip install requests beautifulsoup4
```
    
## Usage
1. Open the scraper.py file.
2. Set the url variable to the desired Amazon search results page URL.
3. Specify the number of pages to scrape by setting the num_pages variable.
4. Run the script:
```python
python scraper.py

```
5. Once the script finishes execution, the scraped product data will be saved in the product_data.csv file.


## License

[MIT](https://choosealicense.com/licenses/mit/)

