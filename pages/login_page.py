from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        user_email = self.browser.find_element(*LoginPageLocators.USER_EMAIL).send_keys(email)
        user_password = self.browser.find_element(*LoginPageLocators.USER_PASSWORD).send_keys(password)
        user_password_repeat = self.browser.find_element(*LoginPageLocators.USER_PASSWORD_REPEAT).send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        register_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, (f"подстрока 'login' отсутcтвует в текущем "
                                                     f"url {self.browser.current_url} браузера")

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "форма логина не найдена на странице"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "форма регистрации не найдена на странице"
