from bs4 import BeautifulSoup
import requests
import datetime
import time
import pandas


URL = [
    "https://www.moneycontrol.com/mutual-funds/nav/icici-prudential-all-seasons-bond-fund-direct-plan-growth/MPI1152",
    "https://www.moneycontrol.com/mutual-funds/nav/icici-prudential-nifty-index-fund-direct-plan-growth/MPI1144",
    "https://www.moneycontrol.com/mutual-funds/nav/icici-prudential-long-term-equity-fund-tax-saving-direct-plan-growth/MPI1126",
    "https://www.moneycontrol.com/mutual-funds/nav/icici-prudential-mnc-fund-direct-plan/MPI4427",
    "https://www.moneycontrol.com/mutual-funds/nav/icici-prudential-esg-fund-direct-plan/MPI4488"
]
NAME = ["BOND", "NIFTY", "EQUITY", "MNC", "ESG"]


def get_today_stock():
    nav = []
    date_value = datetime.date.today().strftime("%d/%m/%Y")
    date = [date_value, date_value, date_value, date_value, date_value]
    i = 0
    while i < 5:
        response = requests.get(URL[i])
        time.sleep(2)
        soup = BeautifulSoup(response.text, "html.parser")
        nav.append(soup.select_one(".leftblok .amt").text.strip("₹ "))
        i += 1
    dataframe = {"Date": date, "Fund Name": NAME, "NAV": nav}
    data = pandas.read_csv("Mutual_Fund_Data.csv")
    if data.iloc[-1]["Date"] != datetime.date.today().strftime("%d/%m/%Y"):
        df = pandas.DataFrame(dataframe)
        # noinspection PyTypeChecker
        df.to_csv("Mutual_Fund_Data.csv", mode="a", header=False)
        print(dataframe)
        print("Written to file")
    else:
        print(dataframe)
        print("Duplicate data, not written to file")


get_today_stock()


