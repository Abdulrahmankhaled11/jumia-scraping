from time import time
from requests_html import HTMLSession
import csv
import time

session = HTMLSession()
product_id = 1
with open('Jumia_products.csv','w',encoding="utf-8",newline='') as file:#context manager

    writer = csv.writer(file)
    writer.writerow(['id','product_name','brand','price','reviews_count','avg_rate'])
    for x in range(1,51):
        print(f'page number {x} .......')

        page  = session.get(f"https://www.jumia.com.eg/all-products/?page={x}#catalog-listing")
        #print(page)

        all_products=page.html.xpath("/html/body/div/main/div[2]/div[3]/section/div[1]",first=True)

        for product in all_products.absolute_links:
            #print(product)
            product_page = session.get(product)
            try:
                product_name = product_page.html.find('h1.-pbxs', first=True).text
            except:
                product_name = ''
            try:
                price = product_page.html.find('span.-fs24', first=True).text
            except:
                price = ''
            try:
                reviews = product_page.html.find('p.-pts', first=True).text
            except:
                reviews = ''
            try:
                avg_rate = product_page.html.find('div.-yl5', first=True).text
            except:
                avg_rate = ''
            try:
                brand = product_page.html.xpath('/html/body/div[1]/main/div[1]/section/div/div[2]/div[2]/div[1]/a[1]', first=True).text
            except:
                brand = ''

            print(product_id,product_name, price,reviews,avg_rate,brand)
           
            writer.writerow([product_id,product_name,brand,price,reviews, avg_rate])
            product_id += 1
        print(product_id  ) 
        print('-----------------------------------------')