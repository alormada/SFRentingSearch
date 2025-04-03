import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os

load_dotenv()

URL = os.environ["FORMS_LINK"]

class FormsUpload:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver()
