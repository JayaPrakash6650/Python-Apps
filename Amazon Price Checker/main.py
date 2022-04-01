from bs4 import BeautifulSoup
import smtplib
import requests


MY_EMAIL = "someone@somewhere.com"
MY_PASSWORD = "something"
REQ_PRICE = 5000.00


def send_mail(to_address, price_drop):

    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=to_address,
            msg=f"Subject:16GB RAM price drop!!!\n\nLook! The price of your RAM card has dropped to Rs.{price_drop}!\nGo check it out now through the link below:\nhttps://www.amazon.in/CORSAIR-Vengeance-1x16GB-3200MHZ-Desktop/dp/B07W8ZDDKT/ref=sr_1_3?keywords=16gb%2Bram%2Bddr4&qid=1638443859&sr=8-3&th=1"
        )

response = requests.get(
    headers={"Accept-Language": "en-US,en;q=0.5",
             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0"},
    url="https://www.amazon.in/CORSAIR-Vengeance-1x16GB-3200MHZ-Desktop/dp/B07W8ZDDKT/ref=sr_1_3?keywords=16gb%2Bram%2Bddr4&qid=1638443859&sr=8-3&th=1"
)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

current_price = soup.find(id="priceblock_ourprice")
price_list = current_price.text.split("₹")[1].split(",")
price = float(price_list[0]+price_list[1])

if price < REQ_PRICE:
    send_mail("someone@somewhere.com", price)
