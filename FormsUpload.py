import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os

load_dotenv()

URL = os.environ["FORMS_LINK"]

class FormsUpload:
    def __init__(self, data):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(URL)
        self.fulfill_forms(data)

    def fulfill_forms(self, data):
        for i in range(len(data.links)):
            time.sleep(1)
            address = self.driver.find_element(By.XPATH,
            value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            address.send_keys(data.addresses[i])

            price = self.driver.find_element(By.XPATH,
            value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price.send_keys(data.prices[i])

            link = self.driver.find_element(By.XPATH,
            value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link.send_keys(data.links[i])

            submit = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
            submit.click()

            if i < len(data.links) - 1:
                time.sleep(1)
                next_offer = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
                next_offer.click()
