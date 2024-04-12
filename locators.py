from selenium.webdriver.common.by import By


class MainPageLocators:
    CURRENT_SECTION = [By.XPATH, ".//div[contains(@class, 'current')]/span"]  # Текущий раздел
    LK = [By.XPATH, ".//a[@href='/account']"]  # Личный кабинет в хэдере
    CONSTRUCTOR = [By.XPATH, ".//a[contains(@class, 'AppHeader_header__link')][@href='/']"]  # Ссылка на Конструктор
    LOGO = [By.XPATH, ".//div[contains(@class, 'AppHeader_header__logo')]/a"]  # Ссылка на конструктор из логотипа
    ORDER_BUTTON = [By.XPATH, ".//button[contains(@class, 'button_button_size_large') and text()='Оформить заказ']"]
    # Кнопка Оформить заказ на главной
    BUILD_A_BURGER = [By.XPATH, ".//h1[text()='Соберите бургер']"]  # Надпись Соберите бургер
    BREAD = [By.XPATH, "//span[@class='text text_type_main-default' and text() = 'Булки']"]  # Раздел Булки
    SAUCES = [By.XPATH, "//span[@class='text text_type_main-default' and text() = 'Соусы']"]  # Раздел Соусы
    TOPPING = [By.XPATH, "//span[@class='text text_type_main-default' and text() = 'Начинки']"]  # Раздел Начинки
    LOGIN_ACCOUNT_BUTTON = [By.XPATH,
                            ".//button[contains(@class, 'button_button_size_large') and text()='Войти в аккаунт']"]
    # Кнопка Войти в аккаунт на Главной


class RegistrationPageLocators:

    REGISTRATION_INPUT_NAME = [By.XPATH, ".//label[text()='Имя']/../input"]  # Регистрация поле Имя
    REGISTRATION_INPUT_EMAIL = [By.XPATH, ".//label[text()='Email']/../input"]  # Регистрация поле Email
    REGISTRATION_INPUT_PASSWORD = [By.XPATH, ".//input[@type='password']"]  # Регистрация поле Пароль
    REGISTER_BUTTON = [By.XPATH, ".//button[text()='Зарегистрироваться']"]  # Кнопка Зарегистрироваться
    INCORRECT_PASSWORD_ERROR = \
        [By.XPATH, ".//p[contains(@class, 'input__error text') and text()='Некорректный пароль']"]
    # Надпись некорректный пароль при регистрации
    LOGIN = [By.XPATH, ".//a[@href='/login']"]  # Ссылка на Вход со страницы регистрации и восстановления пароля


class AutorizationPageLocators:

    LOGIN_INPUT_EMAIL = [By.XPATH, ".//label[text()='Email']/../input"]  # Вход поле Email
    LOGIN_INPUT_PASSWORD = [By.XPATH, ".//label[text()='Пароль']/../input"]  # Вход поле Пароль

    LOG_ON_BUTTON = [By.XPATH, ".//button[contains(@class, 'button_button_size_medium') and text()='Войти']"]
    # Вход кнопка Войти
    REGISTER = [By.XPATH, ".//a[@href='/register']"]  # Зарегистрироваться
    RESTORE_PASSWORD = [By.XPATH, ".//a[@href='/forgot-password']"]  # Восстановить пароль


class LkLocators:
    EXIT_BUTTON = [By.XPATH, ".//button[contains(@class, 'Account_button')][text()='Выход']"]
    # Кнопка Выход из Личного кабинета
    PROFILE_IN_LK = [By.XPATH, ".//a[@href='/account/profile' and text()='Профиль']"]  # Профиль в Личном кабинете
