import smtplib
import requests
from datetime import datetime
import time


MY_LATITUDE = 13
MY_LONGITUDE = 80
MY_LOCATION = {
    "lat": MY_LATITUDE,
    "long": MY_LONGITUDE,
    "formatted": 0,
}
MY_EMAIL = "someone@somewhere.com"
MY_PASSWORD = "something"


def send_mail():

    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:ISS is visible\n\nLook up in the sky! the ISS is visible right now"
        )


def is_iss_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_latitude = float(iss_response.json()["iss_position"]["latitude"])
    iss_longitude = float(iss_response.json()["iss_position"]["longitude"])
    if MY_LATITUDE-5 <= iss_latitude <= MY_LATITUDE+5 and MY_LONGITUDE-5 <= iss_longitude <= MY_LONGITUDE+5:
        return True


def is_dark():
    sun_response = requests.get(url="https://api.sunrise-sunset.org/json", params=MY_LOCATION)
    sun_response.raise_for_status()
    sunrise_time = int(sun_response.json()["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_time = int(sun_response.json()["results"]["sunset"].split("T")[1].split(":")[0])
    current_time = datetime.now().hour
    if current_time >= sunset_time or current_time <= sunrise_time:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_dark():
        send_mail()
