# UI_pages/Search_UI_page.py
import allure
from pages.base_page import BasePage
from locators.locators import MainPageLocators, SearchLocators


class Search(BasePage):
    """
    Класс для работы с поиском на сайте
    """
    
    def __init__(self, driver):
        super().__init__(driver)
        self.main_locators = MainPageLocators()
        self.search_locators = SearchLocators()
        self.driver.get("https://www.kinopoisk.ru/")
        self.wait_main_page()

    @allure.step("Подождать загрузки главной страницы")
    def wait_main_page(self) -> None:
        """
        Ожидает загрузки главной страницы сайта
        """
        self.wait_captcha_disappear()
        self.wait_for_element(self.main_locators.SEARCH_FIELD)

    @allure.step("Ввести поисковый запрос: {name}")
    def input_name(self, name: str) -> None:
        """
        Вводит текст в поле поиска
        """
        self.enter_text(self.main_locators.SEARCH_FIELD, name)

    @allure.step("Нажать кнопку поиска")
    def click_search_button(self) -> None:
        """
        Нажимает на кнопку поиска
        """
        self.click_element(self.main_locators.SEARCH_BUTTON)

    @allure.step("Подождать результатов поиска")
    def wait_search_results(self) -> None:
        """
        Ожидает появления результатов поиска
        """
        self.wait_for_element(self.search_locators.SEARCH_RESULTS)

    @allure.step("Подождать списка подсказок")
    def wait_search_tips(self) -> None:
        """
        Ожидает появления списка подсказок
        """
        self.wait_for_element(self.search_locators.SEARCH_TIPS)

    @allure.step("Получить название первого результата поиска")
    def get_first_result_title(self) -> str:
        """
        Возвращает название первого результата поиска
        """
        return self.get_element_text(self.search_locators.FIRST_RESULT_TITLE)

    @allure.step("Получить сообщение 'Ничего не найдено'")
    def get_no_results_message(self) -> str:
        """
        Возвращает сообщение об отсутствии результатов
        """
        return self.get_element_text(self.search_locators.NO_RESULTS_MESSAGE)

    @allure.step("Получить первую подсказку из списка")
    def get_first_tip(self) -> str:
        """
        Возвращает текст первой подсказки из выпадающего списка
        """
        return self.get_element_text(self.search_locators.FIRST_TIP)

    @allure.step("Выполнить поиск: {query}")
    def search(self, query: str) -> None:
        """
        Выполняет полный процесс поиска
        """
        self.input_name(query)
        self.click_search_button()
        self.wait_search_results()

    @allure.step("Проверить, что найден результат для: {expected_query}")
    def is_result_found(self, expected_query: str) -> bool:
        """
        Проверяет, что найден результат по запросу
        """
        try:
            title = self.get_first_result_title()
            return expected_query.lower() in title.lower()
        except Exception:
            return False

    @allure.step("Проверить, что результаты отсутствуют")
    def is_no_results(self) -> bool:
        """
        Проверяет, что результаты не найдены
        """
        try:
            message = self.get_no_results_message()
            return bool(message)
        except Exception:
            return False

    @allure.step("Получить подсказки для запроса: {query}")
    def get_search_tips(self, query: str) -> str:
        """
        Получает подсказки для поискового запроса
        """
        self.input_name(query)
        self.wait_search_tips()
        return self.get_first_tip()

    @allure.step("Проверить, что URL соответствует ожидаемому: {expected_url}")
    def is_url_matches(self, expected_url: str) -> bool:
        """
        Проверяет соответствие текущего URL ожидаемому
        """
        current_url = self.get_current_url()
        return current_url == expected_url

    @allure.step("Выполнить поиск случайного фильма")
    def search_random_movie(self) -> None:
        """
        Выполняет поиск случайного фильма (пустой поиск)
        """
        self.click_search_button()