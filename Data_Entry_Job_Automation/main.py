import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

ZILLOW_SEARCH_URL = "https://www.zillow.com/san-francisco-ca/rentals/1-_beds/1.0-_baths/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.61529005957031%2C%22east%22%3A-122.25136794042969%2C%22south%22%3A37.703343724016136%2C%22north%22%3A37.847169233586946%7D%2C%22mapZoom%22%3A11%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22baths%22%3A%7B%22min%22%3A1%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
GOOGLE_FORM_URL = YOUR GOOGLE FORM URL
CHROME_DRIVER_PATH = YOUR LOCAL CHROME DRIVER PATH

LIST_OF_ADDRESS = []
LIST_OF_PRICES = []
LIST_OF_LINKS = []

#header differs from machine to machine
header = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Accept-Language" : "en-US,en;q=0.9"
}

response = requests.get(ZILLOW_SEARCH_URL, headers = header)
data = response.text

soup = BeautifulSoup(data, "html.parser")

all_li = soup.select("#grid-search-results .photo-cards_short li article .list-card-info")

#Getting Links
for li in all_li:
    try:
        link = li.select("a")[0]["href"]
        if "https" not in link:
            link = "https://www.zillow.com" + link
        LIST_OF_LINKS.append(link)
    except:
        pass
print(LIST_OF_LINKS)
print(len(LIST_OF_LINKS))

#Getting Addresses
al = soup.select(".list-card-info address")
LIST_OF_ADDRESS = [addr.get_text() for addr in al]
print(LIST_OF_ADDRESS)
print(len(LIST_OF_ADDRESS))

#Getting Prices
ap = soup.select(".list-card-heading")
for price in ap:
    try:
        p = price.get_text().split('/')[0]
        if len(p) > 1:
            LIST_OF_PRICES.append(p)
    except:
        pass
print(LIST_OF_PRICES)
print(len(LIST_OF_PRICES))


#Filling Google Form
driver = webdriver.Chrome(executable_path= CHROME_DRIVER_PATH)
for i in range(len(LIST_OF_PRICES)):
    time.sleep(2)
    link = LIST_OF_LINKS[i]
    address = LIST_OF_ADDRESS[i]
    price = LIST_OF_PRICES[i]

    driver.get(GOOGLE_FORM_URL)

    address_field = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]'
                                                      '/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_field = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/'
                                                    'div/div[2]/div/div[1]/div/div[1]/input')
    link_field = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/'
                                                   'div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/'
                                                 'div/div/span/span')
    address_field.send_keys(address)
    price_field.send_keys(price)
    link_field.send_keys(link)
    submit_button.click()





