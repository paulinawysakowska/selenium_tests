from behave_classy import step_impl_base
from selenium.webdriver.common.by import By

from config import get_config
from environment import get_string
from test_methods import find_element

Base = step_impl_base()
config = get_config()


class AllegroMainPage(Base):
    RODO_POPUP = (By.ID, "dialog-title")
    RODO_POPUP_AGREE_BUTTON = (By.XPATH, "//*[.='Ok, zgadzam się']")
    RODO_POPUP_NOT_AGREE_BUTTON = (By.XPATH, "//*[.='Nie zgadzam się']")
    RODO_POPUP_CHANGE_AGREEMENT_BUTTON = (By.XPATH, "//*[.=""]")
    ALLEGRO_MAIN_PAGE_TITLE = (By.CLASS_NAME, "m7er_80 mpof_ki mli2_0 _13850_1vqFc _13850_NiQLA")

    @Base.step("Komunikat RODO na stronie Allegro jest widoczny")
    def check_allegro_rodo_popup(self):
        allegro_rodo_popup = find_element(self.RODO_POPUP).text
        assert allegro_rodo_popup == get_string("allegro_rodo_popup")

    @Base.step("Użytkownik wyrazi zgodę na przetwarzanie danych")
    def select_rodo_agree_button(self):
        find_element(self.RODO_POPUP_AGREE_BUTTON).click

    @Base.step("Strona główna Allegro jest widoczna")
    def check_allegro_main_page(self):
        allegro_main_page_title = find_element(self.ALLEGRO_MAIN_PAGE_TITLE).text
        assert allegro_main_page_title == get_string("allegro_title2")
