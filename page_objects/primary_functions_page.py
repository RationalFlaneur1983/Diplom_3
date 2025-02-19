from page_objects.base_page import BasePage
from helpers.locators import Locators
import allure


class PrimaryFunctionsPage(BasePage):
    @allure.step("Проверить, что попап с деталями ингредиента отображается")
    def is_ingredient_popup_displayed(self):
        popup = self.find_element(Locators.INGREDIENT_POPUP)
        return "visible" in popup.get_attribute('visibility')



