from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Sprint_5.qa_python_sprint_5.locators import AutorizationPageLocators, MainPageLocators
from Sprint_5.User_data import UserData


class TestCrossing:
    def test_crossing_to_lk_after_login(self, driver):
        (WebDriverWait(driver, 3).
         until(expected_conditions.visibility_of_element_located(MainPageLocators.LOGIN_ACCOUNT_BUTTON)))
        driver.find_element(MainPageLocators.LOGIN_ACCOUNT_BUTTON).click()
        (WebDriverWait(driver, 3).
         until(expected_conditions.visibility_of_element_located(AutorizationPageLocators.LOG_ON_BUTTON)))
        driver.find_element(AutorizationPageLocators.LOGIN_INPUT_EMAIL).send_keys(UserData.current_user.get('email'))
        driver.find_element(AutorizationPageLocators.LOGIN_INPUT_PASSWORD).send_keys(UserData.current_user.get('password'))
        driver.find_element(AutorizationPageLocators.LOG_ON_BUTTON).click()
        (WebDriverWait(driver, 3).
         until(expected_conditions.visibility_of_element_located(MainPageLocators.LOGIN_ACCOUNT_BUTTON)))
        driver.find_element(MainPageLocators.LOGIN_ACCOUNT_BUTTON).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    def test_crossing_to_constructor_after_login(self, driver):
        (WebDriverWait(driver, 3).
         until(expected_conditions.visibility_of_element_located(MainPageLocators.LOGIN_ACCOUNT_BUTTON)))
        driver.find_element(MainPageLocators.LOGIN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(AutorizationPageLocators.LOG_ON_BUTTON))
        driver.find_element(AutorizationPageLocators.LOGIN_INPUT_EMAIL).send_keys(UserData.current_user.get('email'))
        driver.find_element(AutorizationPageLocators.LOGIN_INPUT_PASSWORD).send_keys(UserData.current_user.get('password'))
        driver.find_element(AutorizationPageLocators.LOG_ON_BUTTON).click()
        (WebDriverWait(driver, 3).
         until(expected_conditions.visibility_of_element_located(MainPageLocators.LOGIN_ACCOUNT_BUTTON)))
        driver.find_element(MainPageLocators.LOGIN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MainPageLocators.CONSTRUCTOR))
        driver.find_element(MainPageLocators.CONSTRUCTOR).click()
        assert driver.find_element(MainPageLocators.BUILD_A_BURGER).text == 'Соберите бургер'

    def test_crossing_to_constructor_by_logo(self, driver):
        (WebDriverWait(driver, 3).
         until(expected_conditions.visibility_of_element_located(MainPageLocators.LOGIN_ACCOUNT_BUTTON)))
        driver.find_element(MainPageLocators.LOGIN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(AutorizationPageLocators.LOG_ON_BUTTON))
        driver.find_element(AutorizationPageLocators.LOGIN_INPUT_EMAIL).send_keys(UserData.current_user.get('email'))
        driver.find_element(AutorizationPageLocators.LOGIN_INPUT_PASSWORD).send_keys(UserData.current_user.get('password'))
        driver.find_element(AutorizationPageLocators.LOG_ON_BUTTON).click()
        (WebDriverWait(driver, 3).
         until(expected_conditions.visibility_of_element_located(MainPageLocators.LOGIN_ACCOUNT_BUTTON)))
        driver.find_element(MainPageLocators.LOGIN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MainPageLocators.LOGO))
        driver.find_element(MainPageLocators.LOGO).click()
        assert driver.find_element(MainPageLocators.BUILD_A_BURGER).text == 'Соберите бургер'
