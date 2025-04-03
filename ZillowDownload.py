from dotenv import load_dotenv
import requests
import os
from bs4 import BeautifulSoup



load_dotenv()
URL = os.environ["ZILLOW_WEBSITE"]


class ZillowDownload:
    def __init__(self):
        self.zillow_webpage = requests.get(url=URL)
        self.zillow_webpage = BeautifulSoup(self.zillow_webpage.text, "html.parser")
        self.links = []
        self.addresses = []
        self.prices = []
        self.get_data()
        # print(self.zillow_webpage)

    def get_data(self):
        self.links = [li.a["href"] for li in self.zillow_webpage.find_all("li",
                    class_="ListItem-c11n-8-84-3-StyledListCardWrapper")]

        self.addresses = [li.address.string.strip() for li in self.zillow_webpage.find_all("li",
                    class_="ListItem-c11n-8-84-3-StyledListCardWrapper")]
        self.prices = [li.find("span", class_="PropertyCardWrapper__StyledPriceLine").string.split("/")[0].split("+")[0].replace("$", "") for li in self.zillow_webpage.find_all("li",
                    class_="ListItem-c11n-8-84-3-StyledListCardWrapper")]

        # print(self.links)
        # print(self.addresses)
        # print(self.prices)
        # print(len(self.links), len(self.addresses), len(self.prices))




page = ZillowDownload()
page.get_data()