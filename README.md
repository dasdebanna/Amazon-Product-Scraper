# Amazon Product Scraper

This project is a Python-based web scraper designed to extract product listings and details from Amazon.in. It uses the `requests` library for HTTP requests and `BeautifulSoup` for parsing HTML content.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Detailed Description](#detailed-description)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Product Listing Extraction**: Retrieves product name, URL, price, rating, number of reviews, description, ASIN, and manufacturer.
- **CSV Export**: Exports scraped data to a CSV file for further analysis and processing.
- **Configurable Parameters**: Allows specifying the search query and the number of pages to scrape.

## Technologies Used
- **Python 3.11.3**
- **Requests Library**
- **BeautifulSoup Library**

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/dasdebanna/Amazon-Product-Scraper.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Amazon-Product-Scraper
    ```
3. Install the required libraries:
    ```bash
    pip install requests beautifulsoup4
    ```

## Usage
1. Open the `scraper.py` file.
2. Set the `url` variable to the desired Amazon search results page URL:
    ```python
    url = 'https://www.amazon.in/s?k=product'
    ```
3. Specify the number of pages to scrape by setting the `num_pages` variable:
    ```python
    num_pages = 5
    ```
4. Run the script:
    ```bash
    python scraper.py
    ```
5. The scraped product data will be saved in the `product_data.csv` file.

## Project Structure
- `scraper.py`: Main script for scraping Amazon product data.
- `product_data.csv`: Output file containing the scraped product data.

## Detailed Description
The `scraper.py` script performs the following steps:
1. **Fetch HTML Content**: Uses the `requests` library to get the HTML content of the Amazon search results page.
2. **Parse HTML Content**: Utilizes `BeautifulSoup` to parse the HTML and extract product details.
3. **Extract Data**: Gathers information such as product name, URL, price, rating, number of reviews, description, ASIN, and manufacturer.
4. **Store Data**: Stores the extracted data in a list of dictionaries.
5. **Export to CSV**: Writes the collected data to a CSV file for easy analysis and processing.

### Code Overview
- **Fetching HTML Content**: 
    ```python
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    ```
- **Extracting Data**: 
    ```python
    product_name = item.find('span', class_='a-size-medium a-color-base a-text-normal').text
    product_url = 'https://www.amazon.in' + item.find('a', class_='a-link-normal')['href']
    price = item.find('span', class_='a-price-whole').text
    ```
- **Writing to CSV**: 
    ```python
    with open('product_data.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(products)
    ```

## Contributing
Contributions are welcome! Please follow these steps to contribute:
1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-branch
    ```
3. Make your changes and commit them:
    ```bash
    git commit -m "Add new feature"
    ```
4. Push to the branch:
    ```bash
    git push origin feature-branch
    ```
5. Create a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
