from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), "Basket is not empty, but should be"

    def remove_1st_item_from_basket(self):
        self.go_to_basket()
        quantity = self.browser.find_element(*BasketPageLocators.NUM_FIELD)
        quantity.clear()
        quantity.send_keys("0")
        update_quantity = self.browser.find_element(*BasketPageLocators.UPDATE_QUANTITY)
        update_quantity.click()
