# locators/locators.py
class MainPageLocators:
    """Локаторы главной страницы"""
    USER_CONTAINER = "div.styles_userContainer__hLiRQ"
    SEARCH_FIELD = "input[name=kp_query]"
    SEARCH_BUTTON = "button.styles_root__CUh_v"


class AuthorizationLocators:
    """Локаторы страницы авторизации"""
    LOGIN_BUTTON = "button.styles_loginButton__LWZQp"
    LOGIN_FIELD = "#passp-field-login"
    ENTER_BUTTON = "div.passp-sign-in-button button.Button2"
    ERROR_MESSAGE = "div.Textinput-Hint"
    PHONE_TABS = "div.AuthLoginInputToggle-type"
    PHONE_FIELD = "#passp-field-phone"
    GOOGLE_BUTTON = 'button[data-t="button:pseudo:social:auth:gg"]'
    FORWARD_ROUTE = "div.passp-route-forward"


class SearchLocators:
    """Локаторы для поиска"""
    SEARCH_RESULTS = "div.search_results"
    FIRST_RESULT_TITLE = "div.info p.name"
    NO_RESULTS_MESSAGE = "h2.textorangebig"
    SEARCH_TIPS = "div[data-tid=e4233b06]"
    FIRST_TIP = "a.styles_mainLink__A4Xkh"


class CommonLocators:
    """Общие локаторы"""
    LOADING_SPINNER = "div.loading-spinner"
    CAPTCHA_PAGE = "https://www.kinopoisk.ru/showcaptcha"