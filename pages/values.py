# UI_pages/values.py
"""
Конфигурационные параметры и текстовые константы для UI тестов
"""

# Данные для авторизации
email = ""

# URL
expected_url = "https://passport.yandex.ru/auth/welcome"
random_movie_url = "https://www.kinopoisk.ru/chance/"
base_url = "https://www.kinopoisk.ru/"

# Текстовые сообщения
nothing_found_text = "К сожалению, по вашему запросу ничего не найдено..."
error_login = "Логин не указан"
error_number = "Недопустимый формат номера"

# Тестовые данные
VALID_MOVIE_NAMES = [
    "Хоббит",
    "преступление и наказание", 
    "1+1",
    "И снова здравствуйте!"
]

INVALID_MOVIE_NAMES = [
    "!!!!%",
    "синхрофазатрон"
]

INVALID_PHONE_NUMBERS = [
    "+71111111111",
    "+7 (912) 345-67-890123",
    "+7 (912) 345-67-8"
]