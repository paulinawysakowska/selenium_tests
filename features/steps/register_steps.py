from features.steps.allegro_main_page_view import AllegroMainPage
from features.steps.base_steps import BaseSteps
from features.steps.searching_results_view import SearchingResult

BaseSteps().register()
SearchingResult().register()
AllegroMainPage().register()
