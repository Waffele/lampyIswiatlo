import requests
from bs4 import BeautifulSoup
import pandas as pd
import random

baseurl = "https://www.lampyiswiatlo.pl/"
headers1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/89.0.4389.82 Safari/537.36'}


def get_product_id(product):
    return product.find("div", {"class": "price-box price-final_price"}).get('data-product-id')


def get_product_price(product):
    id = get_product_id(product)
    id = 'old-price-' + id
    return product.find("span", {"id": id}).get('data-price-amount')


def get_product_name(product):
    return product.find("a", {"class": "product-item-link"}).get('title')


def get_page(product):
    link = product.find("a", {"class": "product-item-link"}).get('href')
    k = requests.get(link, headers=headers1).text
    return BeautifulSoup(k, 'html.parser')


def get_product_producer(soup):
    souplist = soup.find("li", attrs={"class": "item-top brand-item"})
    producer = souplist.findAll("span")

    return producer[1].text


def get_logo_image(product):
    return product.find("img").get('data-src')


def get_full_image(soup):
    souplist = soup.find("div", attrs={"class": "product media"})
    return souplist.find("img").get('src')


def get_EAN(soup):
    souplist = soup.find("table", attrs={"class": "data table additional-attributes"})
    return souplist.find("td", {"data-td": "EAN"}).text


def get_style(soup):
    souplist = soup.find("table", attrs={"class": "data table additional-attributes"})
    return souplist.find("td", {"data-td": "Styl"}).text


def get_shape(soup):
    souplist = soup.find("table", attrs={"class": "data table additional-attributes"})
    return souplist.find("td", {"data-td": "Kształt"}).text


def get_description(soup):
    souplist = soup.find("div", attrs={"class": "value"})
    if souplist is not None:
        return souplist.text
    return "Brak opisu"


if __name__ == '__main__':

    index = 1
    products = []
    url_temp = ''
    category = ''

    for x in range(1, 5):

        if x == 1:
            url_temp = 'https://www.lampyiswiatlo.pl/oswietlenie-wewnetrzne/lampy-wiszace'
            category = 'Lampy wiszące'
        elif x == 2:
            url_temp = 'https://www.lampyiswiatlo.pl/oswietlenie-wewnetrzne/kinkiety'
            category = 'Kinkiety'
        elif x == 3:
            url_temp = 'https://www.lampyiswiatlo.pl/oswietlenie-wewnetrzne/lampy-stolowe'
            category = 'Lampy stołowe'
        else:
            url_temp = 'https://www.lampyiswiatlo.pl/lampy-zewnetrzne'
            category = 'Lampy zewnętrzne'

        for i in range(1, 5):
            url = url_temp
            if i != 1:
                url = url + '?p=' + str(i)

            k = requests.get(url, headers=headers1).text
            soup = BeautifulSoup(k, 'html.parser')
            productlist = soup.find_all("li", attrs={"class": "item product product-item"})

            for product in productlist:
                pageSoup = get_page(product)

                id = get_product_id(product)
                price = get_product_price(product)
                name = get_product_name(product)
                producer = get_product_producer(pageSoup)
                image_logo = get_logo_image(product)
                image = get_full_image(pageSoup)
                ean = get_EAN(pageSoup)
                # style = get_style(pageSoup)
                shape = get_shape(pageSoup)
                quantity = random.randint(30, 150)
                description = get_description(pageSoup)

                products.append({
                    'Product ID': index,
                    'Active (0/1)': 1,
                    'Name': name,
                    'Categories (x,y,z...)': category,
                    'Price tax excluded': price,
                    'Tax rules ID': 0,
                    'Wholesale price': None,
                    'On sale (0/1)': 0,
                    'Discount amount': None,
                    'Discount percent': None,
                    'Discount from (yyyy-mm-dd)': None,
                    'Discount to (yyyy-mm-dd)': None,
                    'Reference #': None,
                    'Supplier reference #': None,
                    'Supplier': None,
                    'Manufacturer': producer,
                    'EAN13': ean,
                    'UPC': None,
                    'MPN': None,
                    'Ecotax': None,
                    'Width': None,
                    'Height': None,
                    'Depth': None,
                    'Weight': None,
                    'Deliver time of in-stock products': None,
                    'Delivery time of out-of-stock products with allowed orders': None,
                    'Quantity': quantity,
                    'Minimal quantity': None,
                    'Low stock level': None,
                    'Send me an email when the quantity is under this level': None,
                    'Visbility': 'both',
                    'Additional shipping cost': None,
                    'Unity': None,
                    'Unity price': None,
                    'Summary': None,
                    'Description': description,
                    'Tags (x,y,z...)': shape,
                    'Meta title': 'Meta title-' + shape,
                    'Meta keywords': 'Meta keywords-' + shape,
                    'Meta description': 'Meta description-' + shape,
                    'URL rewritten': None,
                    'Text when in stock': 'W magazynie',
                    'Text when backorder allowed': 'Dostępny',
                    'Available for order (0 = No, 1 = Yes)': 1,
                    'Product available date': None,
                    'Product creation date': None,
                    'Show price (0 = No, 1 = Yes)': 1,
                    'Image URLs (x,y,z...)': image + ', ' + image_logo,
                    'Image alt texts (x,y,z...)': name,
                    'Delete existing images (0 = No, 1 = Yes)': 0,
                    'Feature(Name:Value:Position)': None,
                    'Available online only (0 = No, 1 = Yes)': 0,
                    'Condition': 'new',
                    'Customizable (0 = No, 1 = Yes)': 0,
                    'Uploadable files (0 = No, 1 = Yes)': 0,
                    'Text fields (0 = No, 1 = Yes)': 0,
                    'Out of stock action': 0,
                    'Virtual product': 0,
                    'File URL': None,
                    'Number of allowed downloads': None,
                    'Expiration date': None,
                    'Number of days': None,
                    'ID / Name of shop': None,
                    'Advanced stock management': None,
                    'Depends On Stock': None,
                    'Warehouse': None,
                    'Acessories  (x,y,z...)': None
                })

                print(index, ' | category:', category)
                index += 1

    products[0]['On sale (0/1)'] = 1
    products[0]['Discount amount'] = 50

    products[1]['On sale (0/1)'] = 1
    products[1]['Discount percent'] = 20

    df = pd.DataFrame(products)
    df.to_csv('produkty.csv', sep=';', index=False, encoding='utf-8')
