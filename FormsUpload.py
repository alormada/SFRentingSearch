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

    def fulfill_forms(self, data):
        address = self.driver.find_element(By)
        # for i in range(len(data.links)):


forms = FormsUpload()
