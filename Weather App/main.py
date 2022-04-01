import requests
import smtplib

MY_EMAIL = "someone@somewhere.com"
MY_PASSWORD = "something"
RECIPIENTS = ["someone2@somewhere.com",
              "someone3@somewhere.com",
              "someone4@somewhere.com"]
API_ID = "Register at the below URL to get an API ID"
URL = "http://api.openweathermap.org/data/2.5/onecall"
MY_LATITUDE = 13
MY_LONGITUDE = 80
PARAMETERS = {
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    "exclude": "current,minutely,daily",
    "appid": API_ID,
}


def send_mail():
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=RECIPIENTS,
            msg="Subject:Weather Forecast\n\n"
                "There is a chance of rain in the next 12 hours.\n"
                "Bring an umbrella with you if you're going out :)"
            )


response = requests.get(url=URL, params=PARAMETERS)
response.raise_for_status()
weather_data = response.json()["hourly"][:12]
for hour in weather_data:
    if hour["weather"][0]["id"] < 700:
        send_mail()
        break
