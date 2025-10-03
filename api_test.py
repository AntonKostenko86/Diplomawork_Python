# test_api.py
import allure
import pytest
from api.search_page import Search
from api.values_api import my_id, id_error_message

class TestAPISearch:
    """Группировка тестов API поиска в классе"""
    
    @pytest.fixture
    def search_api(self, api):
        return api

    @allure.title("Поиск фильма по id")
    @allure.epic("API тесты")
    @allure.feature("Позитивные тесты")
    @allure.severity("blocker")
    def test_search_by_id_positive(self, search_api: Search):
        # Act
        result = search_api.search_by_id(my_id)
        
        # Assert
        with allure.step("Проверить, что ID совпадает"):
            assert result["id"] == my_id

    @pytest.mark.parametrize("movie_name", [
        "Дракула", "преступление и наказание", "1+1", "И снова здравствуйте!"
    ])
    @allure.title("Поиск фильма по названию на кириллице")
    def test_search_by_name_positive(self, search_api: Search, movie_name):
        # Act
        results = search_api.search_by_name(movie_name)
        
        # Assert
        with allure.step("Проверить, что найден хотя бы один результат"):
            assert len(results) > 0
        with allure.step("Проверить совпадение названия"):
            assert results[0]["name"].lower() == movie_name.lower()

    @pytest.mark.parametrize("movie_name,expected_field", [
        ("Drive", "alternativeName"),
        ("catch me if you can", "alternativeName"),
        ("Schitt$ Creek", "alternativeName")
    ])
    def test_search_by_english_name_positive(self, search_api: Search, movie_name, expected_field):
        results = search_api.search_by_name(movie_name)
        assert len(results) > 0
        assert results[0][expected_field].lower() == movie_name.lower()

class TestAPINegative:
    """Тесты негативных сценариев API"""
    
    @pytest.mark.parametrize("invalid_name", ["синхрофазатрон"])
    def test_search_by_invalid_name(self, api: Search, invalid_name):
        results = api.search_by_name(invalid_name)
        assert len(results) == 0

    def test_search_by_invalid_id(self, api: Search):
        # Act
        result = api.search_by_id("0")
        
        # Assert
        assert result["message"][0] == id_error_message
        assert result["statusCode"] == 400