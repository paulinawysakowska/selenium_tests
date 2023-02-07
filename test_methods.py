from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.google.com/')

DEFAULT_TIMEOUT = 10


def find_element(selector, timeout=DEFAULT_TIMEOUT):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(selector), message='Element: {} - is not visible!'.format(selector[1])
    )


def find_elements(selector, timeout=DEFAULT_TIMEOUT):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_all_elements_located(selector), message='Elements: {} - are not visible!'.format(selector[1])
    )


def click(el):
    driver.execute_script("arguments[0].click();", el)


def send_keys(text):
    ActionChains(driver).send_keys(text).perform()
