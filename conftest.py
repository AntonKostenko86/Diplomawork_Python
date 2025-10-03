import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from api.search_page import Search
from api.values_api import base_url

@pytest.fixture
def driver():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    browser.maximize_window()
    yield browser
    browser.quit()

@pytest.fixture
def api():
    return Search(base_url)

@pytest.fixture
def auth_page(driver):
    from UI_pages.AuthorizationPage import Authorization
    return Authorization(driver)

@pytest.fixture
def search_page(driver):
    from UI_pages.Search_UI_page import Search
    return Search(driver)