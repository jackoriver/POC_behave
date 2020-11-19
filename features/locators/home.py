from selenium.webdriver.common.by import By


class HomeLocators:
    MENU = By.ID, 'menu_button_container'
    CART = By.ID, 'shopping_cart_container'
    CART_ICON = By.CSS_SELECTOR, f"#{CART[1]} svg"
    INVENTORY_SECTION = By.CSS_SELECTOR, '#inventory_container .inventory_container'
