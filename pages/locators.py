from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "[class='btn btn-lg btn-primary btn-add-to-basket']")
    BASKET_VALUE_MESSAGE = (By.XPATH, "//div[@id='messages']/div[3]/div/p/strong")
    BASKET_PRODUCT_NAME = (By.XPATH, "//div[@id='messages']/div[1]/div/strong")
    PRODUCT_NAME = (By.XPATH, "//h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "[class='price_color']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='messages']/div[1]/div[@class='alertinner ']")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//span/a")
    BASKET_ADDED_ITEMS = (By.XPATH, "//div[@class='row']/h2")
    EMPTY_BASKET_MESSAGE = (By.XPATH, "//div/p")

