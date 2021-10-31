import requests
import csv
from bs4 import BeautifulSoup
url="https://www.myhome.ie/residential/sligo/property-for-sale"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

home_file = open('scrapingtest.csv', mode = 'w')
home_writer = csv.writer(home_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

listings = soup.findAll("div", class_= "PropertyListingCard")

for listing in listings:
    entrylist = []

    price = listing.find(class_="PropertyListingCard__Price").text
    entrylist.append(price)
    address = listing.find(class_="PropertyListingCard__Address").text
    entrylist.append(address)

    home_writer.writerow(entrylist)
home_file.close

