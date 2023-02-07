from time import sleep

from behave_classy import step_impl_base
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from config import get_config
from environment import get_string
from features.steps.base_steps import BaseSteps
from test_methods import find_element

Base = step_impl_base()
config = get_config()


class SearchingResult(Base, BaseSteps):
    ALLEGRO_URL = (By.CLASS_NAME, "TbwUpd")
    ALLEGRO_TITLE_TEXT = (By.CLASS_NAME, "LC20lb MBeuO DKV0Md")
    ALLEGRO_TITLE_TEXT2 = (By.CLASS_NAME, "yuRUbf")
    ALLEGRO_COPY_TEXT = (By.CLASS_NAME, "IsZvec")

    @Base.step("Wyniki wyszukiwania są widoczne")
    def check_searching_page(self):
        for _ in range(5):
            try:
                allegro_url = find_element(self.ALLEGRO_URL)
                # allegro_title = find_element(self.ALLEGRO_TITLE_TEXT)
                allegro_copy = find_element(self.ALLEGRO_COPY_TEXT)
                assert allegro_url.is_displayed()
                # assert allegro_title.is_displayed()
                assert allegro_copy.is_displayed()
                break
            except TimeoutException:
                sleep(0.5)
        else:
            raise TimeoutException("Error while checking input filed")
        assert allegro_url.text == get_string("allegro_url")
        # assert allegro_title.text == get_string("allegro_title")
        assert allegro_copy.text == get_string("allegro_copy")

    @Base.step("Użytkownik wybierze jeden z wyników wyszukiwania")
    def select_searching_result(self):
        for _ in range(15):
            try:
                searching_result = find_element(self.ALLEGRO_TITLE_TEXT2)
                searching_result.click()
                break
            except TimeoutException:
                sleep(1)
        else:
            raise TimeoutException("Error while checking page")

