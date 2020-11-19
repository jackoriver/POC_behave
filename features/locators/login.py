from selenium.webdriver.common.by import By


class LoginLocators:
    USERNAME = By.CSS_SELECTOR, "[data-test='username']"
    PASSWORD = By.CSS_SELECTOR, "[data-test='password']"
    LOGIN_BUTTON = By.ID, "login-button"
