from .base_page import BasePage
from .basket_page import BasketPage
# from .locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def should_be_empty_basket(self):
        self.go_to_basket()
        BasketPage.should_be_empty(self)
