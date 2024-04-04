import pytest

from .pages.product_page import ProductPage

main_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


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
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    link = main_link + promo
    page = ProductPage(browser, link)
    page.open()
    name = page.get_product_name()
    price = page.get_product_price()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_with_name_for_added_product(name)
    page.should_be_message_with_price_for_added_product(price)
