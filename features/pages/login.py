from features.locators.login import LoginLocators
from features.pages.base_page import BasePage


class LoginPage(BasePage):

    @property
    def username(self):
        return self.driver.find_element(*LoginLocators.USERNAME)

    @property
    def password(self):
        return self.driver.find_element(*LoginLocators.PASSWORD)

    @property
    def login_button(self):
        return self.driver.find_element(*LoginLocators.LOGIN_BUTTON)
