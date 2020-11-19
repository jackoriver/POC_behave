from features.locators.home import HomeLocators
from features.pages.base_page import BasePage


class HomePage(BasePage):
    @property
    def menu_button(self):
        return self.driver.find_element(*HomeLocators.MENU)

    @property
    def cart(self):
        return self.driver.find_element(*HomeLocators.CART_ICON)

    @property
    def inventory_section(self):
        return self.driver.find_element(*HomeLocators.INVENTORY_SECTION)
