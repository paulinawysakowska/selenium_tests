import os
from logging import root
import xml.etree.ElementTree as ET
from selenium.webdriver.chrome import webdriver
import time

root = ET.parse(os.environ.get("APP_TEXT_STRINGS", "app_text_strings.xml")).getroot()


def get_string(name) -> str:
    return root.findtext(path=f"./string/[@name='{name}']")


def before_all():
    driver = webdriver.Chrome()
    driver.get('https://www.google.com/')


# def after_all():
#     driver.quit()
