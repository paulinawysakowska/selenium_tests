from time import sleep

from behave_classy import step_impl_base
from selenium.common import ElementNotInteractableException
from selenium.webdriver.common.by import By

from config import get_config
from environment import get_string
from test_methods import find_element

Base = step_impl_base()
config = get_config()


class BaseSteps(Base):
    BEFORE_YOU_GO_TO_GOOGLE_TITLE = (By.ID, "S3BnEe")
    LANGUAGE_BUTTON = (By.ID, "")
    LOG_IN_BUTTON = (By.ID, "")
    ACCEPT_ALL_BUTTON = (By.ID, "W0wltc")
    REJECT_ALL_BUTTON = (By.ID, "")
    MORE_OPTIONS = (By.CLASS_NAME, "")
    GOOGLE_LOGO = (By.ID, "lnXdpd")
    GOOGLE_INPUT_FILED = (By.CLASS_NAME, "gLFyf")
    GOOGLE_SEARCH_BUTTON = (By.CLASS_NAME, "gNO89b")
    GOOGLE_CAMERA_SEARCH_BUTTON = (By.CLASS_NAME, "Gdd5U")

    @Base.step("Komunikat o przetwarzaniu danych jest widoczny")
    def check_before_go_to_google_page(self):
        before_go_to_google = find_element(self.BEFORE_YOU_GO_TO_GOOGLE_TITLE)
        before_go_to_google.is_displayed()
        assert before_go_to_google.text == get_string("before_you_go_to_google")

    @Base.step("Użytkownik wybierze przycisk Zamknij")
    def select_accept_all_button(self):
        accept_all_button = find_element(self.ACCEPT_ALL_BUTTON)
        accept_all_button.click()

    @Base.step("Strona Google jest widoczna")
    def check_google_logo(self):
        google_search_button = find_element(self.GOOGLE_SEARCH_BUTTON)
        # google_camera_search_button = find_element(self.GOOGLE_CAMERA_SEARCH_BUTTON)
        for _ in range(5):
            try:
                assert google_search_button.is_displayed()
                assert google_search_button.text == get_string("google_search")
                break
            except AssertionError:
                sleep(1)
        else:
            raise AssertionError()

    @Base.step("Użytkownik wybierze przycisk Szukaj w Google")
    def select_google_search_button(self):
        search_button = find_element(self.GOOGLE_SEARCH_BUTTON)
        for _ in range(5):
            try:
                search_button.is_displayed()
                break
            except ElementNotInteractableException:
                sleep(0.1)
        else:
            raise ElementNotInteractableException("Error while checking input filed")

    @Base.step("Wyszukiwana fraza nie jest uzupełniona")
    def check_input_filed(self):
        for _ in range(5):
            try:
                input_filed = find_element(self.GOOGLE_INPUT_FILED)
                assert len(input_filed.text) == 0
                break
            except ElementNotInteractableException:
                sleep(0.1)
        else:
            raise ElementNotInteractableException("Error while checking input filed")

    @Base.step("Użytkownik wyszuka frazę Allegro")
    def paste_searching_phase(self):
        input_filed = find_element(self.GOOGLE_INPUT_FILED)
        input_filed.click()
        input_filed.send_keys(config["searching_phrase"])
        input_filed.submit()

