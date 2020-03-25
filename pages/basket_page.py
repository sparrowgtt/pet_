from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def should_be_empty(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_ADDED_ITEMS), \
            "The element is presented but should not be"

    def should_be_empty_basket_message(self):
        empty_basket_message = self.browser.find_element(*BasePageLocators.EMPTY_BASKET_MESSAGE).text
        if "Your basket is empty" in empty_basket_message:
            return True
        else:
            return False

