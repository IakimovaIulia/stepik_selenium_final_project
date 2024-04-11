import time

import pytest

from pages.basket_page import BasketPage
from pages.locators import ProductPageLocators
from pages.login_page import LoginPage
from .pages.product_page import ProductPage

main_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


@pytest.mark.need_review
@pytest.mark.parametrize('promo', ["?promo=offer0",
                                   "?promo=offer1",
                                   "?promo=offer2",
                                   "?promo=offer3",
                                   "?promo=offer4",
                                   "?promo=offer5",
                                   "?promo=offer6",
                                   pytest.param("?promo=offer7", marks=pytest.mark.xfail),
                                   "?promo=offer8",
                                   "?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, promo):
    link = main_link + promo
    page = ProductPage(browser, link)
    page.open()
    name = page.get_product_name()
    price = page.get_product_price()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_with_name_for_added_product(name)
    page.should_be_message_with_price_for_added_product(price)


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME)


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME)


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME)


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, link)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, link)
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_message_empty_basket()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "123456"
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        name = page.get_product_name()
        price = page.get_product_price()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_message_with_name_for_added_product(name)
        page.should_be_message_with_price_for_added_product(price)

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME)
