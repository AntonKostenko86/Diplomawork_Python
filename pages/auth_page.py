# UI_pages/AuthorizationPage.py
from selenium.webdriver.common.by import By
import allure
from pages.base_page import BasePage
from locators.locators import MainPageLocators, AuthorizationLocators


class Authorization(BasePage):
    """
    Класс для работы со страницей авторизации
    """
    
    def __init__(self, driver):
        super().__init__(driver)
        self.main_locators = MainPageLocators()
        self.auth_locators = AuthorizationLocators()
        self.driver.get("https://www.kinopoisk.ru/")
        self.wait_main_page()

    @allure.step("Подождать загрузки главной страницы")
    def wait_main_page(self) -> None:
        """
        Ожидает загрузки главной страницы сайта
        """
        self.wait_captcha_disappear()
        self.wait_for_element(self.main_locators.USER_CONTAINER)

    @allure.step("Открыть страницу авторизации")
    def open_authorization(self) -> None:
        """
        Открывает страницу авторизации
        """
        self.click_element(self.main_locators.LOGIN_BUTTON)

    @allure.step("Ввести логин: {login}")
    def enter_login(self, login: str) -> None:
        """
        Вводит логин/почту в поле ввода
        """
        self.enter_text(self.auth_locators.LOGIN_FIELD, login)

    @allure.step("Нажать кнопку 'Войти'")
    def click_enter_button(self) -> None:
        """
        Нажимает кнопку 'Войти' на странице авторизации
        """
        self.click_element(self.auth_locators.ENTER_BUTTON)

    @allure.step("Подождать загрузки страницы авторизации")
    def wait_authorization_page(self) -> None:
        """
        Ожидает загрузки страницы авторизации
        """
        self.wait_for_element(self.auth_locators.FORWARD_ROUTE)

    @allure.step("Нажать кнопку 'Войти через Google'")
    def click_google_button(self) -> None:
        """
        Нажимает на кнопку 'Войти через Google'
        """
        self.click_element(self.auth_locators.GOOGLE_BUTTON)

    @allure.step("Подождать открытия всплывающего окна")
    def wait_popup_window(self) -> None:
        """
        Ожидает открытия всплывающего окна
        """
        original_window = self.driver.current_window_handle
        self.wait.until(EC.number_of_windows_to_be(2))
        
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break

    @allure.step("Получить сообщение об ошибке")
    def get_error_message(self) -> str:
        """
        Возвращает текст сообщения об ошибке
        """
        return self.get_element_text(self.auth_locators.ERROR_MESSAGE)

    @allure.step("Переключиться на вкладку 'Телефон'")
    def switch_to_phone_tab(self) -> None:
        """
        Переключается на вкладку ввода телефона
        """
        phone_tabs = self.driver.find_elements(By.CSS_SELECTOR, self.auth_locators.PHONE_TABS)
        if len(phone_tabs) > 1:
            phone_tabs[1].find_element(By.CSS_SELECTOR, "button.Button2").click()

    @allure.step("Ввести номер телефона: {phone_number}")
    def enter_phone_number(self, phone_number: str) -> None:
        """
        Вводит номер телефона в поле ввода
        """
        self.enter_text(self.auth_locators.PHONE_FIELD, phone_number)

    @allure.step("Выполнить авторизацию с логином: {login}")
    def login(self, login: str) -> None:
        """
        Выполняет полный процесс авторизации
        """
        self.open_authorization()
        self.enter_login(login)
        self.click_enter_button()
        self.wait_authorization_page()

    @allure.step("Проверить, что авторизация прошла успешно")
    def is_login_successful(self, expected_url: str) -> bool:
        """
        Проверяет успешность авторизации по URL
        """
        current_url = self.get_current_url()
        return current_url.startswith(expected_url)

    @allure.step("Выполнить авторизацию с телефоном: {phone_number}")
    def login_with_phone(self, phone_number: str) -> None:
        """
        Выполняет попытку авторизации по телефону
        """
        self.open_authorization()
        self.switch_to_phone_tab()
        self.enter_phone_number(phone_number)
        self.click_enter_button()