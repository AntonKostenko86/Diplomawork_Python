# test_ui.py
import pytest
import allure
from pages.values import *

class TestAuthorization:
    """Тесты авторизации"""
    
    @allure.title("Успешная авторизация с валидной почтой")
    @allure.severity("blocker")
    def test_authorization_positive(self, auth_page):
        # Arrange
        auth_page.open_authorization()
        
        # Act
        auth_page.enter_login(email)
        auth_page.click_enter_button()
        auth_page.wait_page("div.passp-route-forward")
        
        # Assert
        current_url = auth_page.get_current_url()
        assert current_url.startswith(expected_url)

    @allure.title("Авторизация с пустым логином")
    def test_authorization_empty_login(self, auth_page):
        auth_page.open_authorization()
        auth_page.enter_login("")
        auth_page.click_enter_button()
        auth_page.wait_page("div.Textinput-Hint")
        
        error = auth_page.error_message()
        assert error == error_login

    @pytest.mark.parametrize("phone_number", [
        "+71111111111",
        "+7 (912) 345-67-890123", 
        "+7 (912) 345-67-8"
    ])
    def test_authorization_invalid_phone(self, auth_page, phone_number):
        auth_page.open_authorization()
        auth_page.click_phone_button()
        auth_page.enter_phone_number(phone_number)
        auth_page.click_enter_button()
        auth_page.wait_page("div.Textinput-Hint")
        
        error = auth_page.error_message()
        assert error == error_number

class TestUISearch:
    """Тесты UI поиска"""
    
    @pytest.mark.parametrize("movie_name", [
        "Хоббит", "преступление и наказание", "1+1", "И снова здравствуйте!"
    ])
    def test_search_positive(self, search_page, movie_name):
        search_page.input_name(movie_name)
        search_page.click_search_button()
        search_page.wait_result("div.search_results")
        
        title = search_page.search_result()
        assert movie_name.lower() in title.lower()

    def test_empty_search_opens_random_movie(self, search_page):
        search_page.click_search_button()
        current_url = search_page.get_current_url()
        assert current_url == random_movie_url