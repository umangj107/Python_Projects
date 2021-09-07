import requests
from bs4 import BeautifulSoup
from notification_manager import NotificationManager

RPB_DESIRED_PRICE = 1700
RPB_AMAZON_URL = "LINK OF AMAZON PRODUCT YOU WANT TO TRACK"
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Accept-Language" : "en-US,en;q=0.9"
}

response = requests.get(RPB_AMAZON_URL, headers=headers)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
# print(soup.prettify())

price = soup.find(name="span", class_="a-size-medium a-color-price priceBlockBuyingPriceString")
# print(int(price.text.split()[1])+1)
price = price.text.split()[1]
current_price = float(''.join(price.split(',')))
print(current_price)



if current_price < RPB_DESIRED_PRICE:
    message = f"\nLow Price Alert! The price of [YOUR DESIRED PRODUCT] " \
              f"has dropped to {current_price}! \nGo ahead and buy before the deal ends !"
    msg = NotificationManager()
    msg.send_sms(message)
    msg.send_emails(message)