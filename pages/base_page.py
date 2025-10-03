# UI_pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from locators.locators import CommonLocators
import allure
import logging

logger = logging.getLogger(__name__)


class BasePage:
    """
    Базовый класс для всех страниц
    """
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)
        self.logger = logger
        self.common_locators = CommonLocators()

    @allure.step("Подождать элемент {locator}")
    def wait_for_element(self, locator: str, timeout: int = 50):
        """
        Ожидает появления элемента на странице
        """
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, locator))
            )
        except TimeoutException:
            self.logger.error(f"Элемент {locator} не появился за {timeout} секунд")
            raise

    @allure.step("Подождать кликабельности элемента {locator}")
    def wait_for_element_clickable(self, locator: str, timeout: int = 50):
        """
        Ожидает, когда элемент станет кликабельным
        """
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, locator))
            )
        except TimeoutException:
            self.logger.error(f"Элемент {locator} не стал кликабельным за {timeout} секунд")
            raise

    @allure.step("Получить текущий URL")
    def get_current_url(self) -> str:
        """
        Возвращает текущий URL
        """
        return self.driver.current_url

    @allure.step("Получить текст элемента {locator}")
    def get_element_text(self, locator: str) -> str:
        """
        Возвращает текст элемента
        """
        element = self.wait_for_element(locator)
        return element.text

    @allure.step("Кликнуть на элемент {locator}")
    def click_element(self, locator: str):
        """
        Кликает на элемент
        """
        element = self.wait_for_element_clickable(locator)
        element.click()

    @allure.step("Ввести текст '{text}' в элемент {locator}")
    def enter_text(self, locator: str, text: str):
        """
        Вводит текст в поле ввода
        """
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Подождать, что URL содержит {expected_url}")
    def wait_url_contains(self, expected_url: str, timeout: int = 50):
        """
        Ожидает, что URL содержит определенную строку
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.url_contains(expected_url)
            )
        except TimeoutException:
            self.logger.error(f"URL не содержит {expected_url} за {timeout} секунд")
            raise

    @allure.step("Подождать исчезновения капчи")
    def wait_captcha_disappear(self):
        """
        Ожидает исчезновения капчи
        """
        try:
            self.wait.until_not(
                EC.url_contains(self.common_locators.CAPTCHA_PAGE)
            )
        except TimeoutException:
            self.logger.warning("Капча не исчезла, продолжаем выполнение")

    @allure.step("Подождать исчезновения спиннера загрузки")
    def wait_loading_disappear(self, timeout: int = 30):
        """
        Ожидает исчезновения спиннера загрузки
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, self.common_locators.LOADING_SPINNER))
            )
        except TimeoutException:
            self.logger.warning("Спиннер загрузки не исчез за отведенное время")