# Find the inventory value of all the books on http://books.toscrape.com

import requests
import bs4

base_url = "http://books.toscrape.com/catalogue/page-{}.html"
res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text, "lxml")
product = soup.select(".product_pod")
example = product[1]
example_price = example.select(".price_color")

# How to get just the price
# for tags in example_price:
# print(tags.text.strip())

book_title_price = []
for page_num in range(1, 50 + 1):

    scrape_url = base_url.format(page_num)
    res = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(res.text, "lxml")
    prices = soup.select(".price_color")

    for price in prices:
        price = price.text.strip()
        price = price.replace("£", "")
        price = price.replace("Â", "")
        book_title_price.append(price)

book_title_price = [float(f) for f in book_title_price]
inventory_total = sum(book_title_price)
print("The inventory value of all the books on http://www.books.toscrape.com is: {}".format(inventory_total))
