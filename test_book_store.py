import time
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
import pytest


@pytest.mark.skip
class TestMainPage:
    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
        time.sleep(1)

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        time.sleep(1)

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_empty_basket()
        time.sleep(1)


@pytest.mark.skip
class TestLoginPage:
    def test_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_page()
        time.sleep(1)


@pytest.mark.skip
class TestProductPageByGuest:
    @pytest.mark.parametrize('link', (f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}" for i in range(0, 10) if i != 7))
    def test_product_page(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
        page.test_can_add_product_to_basket()
        # page.should_be_disappeared_success_message()
        time.sleep(1)

    def test_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()
        time.sleep(1)

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_empty_basket()
        time.sleep(1)


# @pytest.mark.skip
class TestProductPageByUser:   # TestUserAddToBasketFromProductPage
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_page(log=1)  # См.описание функции в login_page.py, чтобы узнать про параметр, если нужно
        page.should_be_authorized_user()
        time.sleep(1)

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/neuromancer_13/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
        page.test_can_add_product_to_basket()
        # page.should_be_disappeared_success_message()
        time.sleep(1)
