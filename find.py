from bs4 import BeautifulSoup
import requests 
import urllib.request
import time
import random
import decimal
import json

headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'My User Agent 1.0',
    'From': 'qwerty@aol.com'
})

city = input("Enter City: ")
stateOrCountry = input("Enter State/Country: ")
adults = input("Enter Number of Adults: ")
beds = input("Enter Number of Beds: ")
checkinyear = input("Checkin Year: ")
checkinmonth = input("Checkin Month: ")
checkinday = input("Checkin Day: ")
checkoutyear = input("Checkout Year: ")
checkoutmonth = input("Checkout Month: ")
checkoutday = input("Checkout Day: ")
checkin = checkinyear + '-' + checkinmonth + '-' + checkinday
checkout = checkoutyear + '-' + checkoutmonth + '-' + checkoutday

class Listing:
  def __init__(self, name, price, adults, beds, checkin, checkout, imgs):
    self.name = name
    self.price = price
    self.adults = adults
    self.beds = beds
    self.imgs = imgs
def getData(city, stateOrCountry, adults, beds, checkin, checkout):
        listArg = list()
        urlArg = ('https://www.expedia.com/Hotel-Search?/adults=' + adults + '&beds=' + beds + '&d1=' + checkin + '/' +
                    '%2F&d2=' + checkout + '%25&destination=' + city + "%20%28and%20vicinity%29%2C%20" + stateOrCountry + '&sort=RECOMMENDED')
        print (urlArg)
        print("\n\n")
        page = requests.get(urlArg, headers=headers)
        soup = BeautifulSoup(page.text, 'lxml')
        price = soup.findAll('span',{'data-stid': 'content-hotel-lead-price'})
        titles = soup.findAll('h3', class_= 'is-visually-hidden')
        externalLink = soup.findAll('a', {'class': 'listing__link uitk-card-link'})
        loopCounter = 0
        if len(titles) > len(price):
            loopCounter = len(price)
        elif len(titles) < len(price):
            loopCounter = len(titles)
        else:
            loopCounter = len(titles)
        for i in range(loopCounter):
            externalLink[i]['href'] = 'https://expedia.com' + externalLink[i]['href']
            listArg.append(Listing(titles[i].text, price[i].text, adults, beds, checkin, checkout, externalLink[i]['href']))
        return (listArg)

def printData(list):
    for item in list:
        print (item.name + "\n" + item.price + "\n" + item.imgs + "\n\n")

hotelList = getData(city, stateOrCountry, adults, beds, checkin, checkout)
printData(hotelList)
