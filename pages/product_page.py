from .base_page import BasePage
from .basket_page import BasketPage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_BASKET_TOTAL), "Success message is presented, but should not be"

    def test_can_add_product_to_basket(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_button.click()
        time.sleep(1)

        # BasePage.solve_quiz_and_get_code(self)
        alert_book_name = self.browser.find_element(*ProductPageLocators.ALERT_BOOK_NAME).text
        assert alert_book_name == book_name, "another book added to basket"
        alert_basket_total = self.browser.find_element(*ProductPageLocators.ALERT_BASKET_TOTAL).text
        assert alert_basket_total == book_price, "invalid price in basket"

        BasketPage.remove_1st_item_from_basket(self)

    def should_be_disappeared_success_message(self):
        alert_basket_total_close_button = self.browser.find_element(*ProductPageLocators.ALERT_BASKET_TOTAL_CLOSE_BUTTON)
        alert_basket_total_close_button.click()
        assert self.is_disappeared(*ProductPageLocators.ALERT_BASKET_TOTAL), "Alert with total price should be closed, but it's not"

    def should_be_empty_basket(self):
        self.go_to_basket()
        BasketPage.should_be_empty(self)
