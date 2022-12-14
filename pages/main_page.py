import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Main_page(Base):

    url = 'https://znyworldwide.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    zny_logo = "//a[@class='header__logo']"
    login_page_button = "//html/body/main/section[1]/div/header/nav/div[1]/ul[3]/li[1]/a"
    hoodies_page_button = "//span[text()='Худи / свитшоты']"
    cart_total_button = "//span[@id='cart-total']"

    # Getters

    def get_zny_logo(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.get_zny_logo)))

    def get_login_page_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_page_button)))

    def get_hoodies_page_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.hoodies_page_button)))

    def get_cart_total_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_total_button)))

    # Actions

    def click_zny_logo(self):
        self.get_zny_logo().click()
        print("Click zny logo")

    def click_login_page_button(self):
        self.get_login_page_button().click()
        print("Click login page button")

    def click_hoodies_page_button(self):
        self.get_hoodies_page_button().click()
        print("Click hoodies page button")

    def click_cart_total_button(self):
        self.get_cart_total_button().click()
        print("Click cart total button")

    # Methods

    def get_driver(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def select_login_page(self):
        with allure.step("Select login page"):
            Logger.add_start_step(method="select_login_page")
            self.get_current_url()
            self.click_login_page_button()
            Logger.add_end_step(url=self.driver.current_url, method="select_login_page")

    def select_hoodies_page(self):
        with allure.step("Select hoodies page"):
            Logger.add_start_step(method="select_hoodies_page")
            self.get_current_url()
            self.click_hoodies_page_button()
            Logger.add_end_step(url=self.driver.current_url, method="select_hoodies_page")

    def select_cart_total_page(self):
        with allure.step("Select cart total page"):
            Logger.add_start_step(method="select_cart_total_page")
            self.get_current_url()
            self.click_cart_total_button()
            Logger.add_end_step(url=self.driver.current_url, method="select_cart_total_page")
