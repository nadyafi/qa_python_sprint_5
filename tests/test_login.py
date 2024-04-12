from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Sprint_5.qa_python_sprint_5.locators import RegistrationPageLocators, AutorizationPageLocators, MainPageLocators
from Sprint_5.User_data import UserData


class TestAutorization:
    def test_login_from_button_in_main_page(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MainPageLocators.LOGIN_ACCOUNT_BUTTON))
        driver.find_element(MainPageLocators.LOGIN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(AutorizationPageLocators.LOG_ON_BUTTON))
        driver.find_element(AutorizationPageLocators.LOGIN_INPUT_EMAIL).send_keys(UserData.current_user.get('email'))
        driver.find_element(AutorizationPageLocators.LOGIN_INPUT_PASSWORD).send_keys(UserData.current_user.get('password'))
        driver.find_element(AutorizationPageLocators.LOG_ON_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
        assert driver.find_element(MainPageLocators.ORDER_BUTTON).text == 'Оформить заказ'

    def test_login_from_lk(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MainPageLocators.LK))
        driver.find_element(MainPageLocators.LK).click()
        driver.find_element(AutorizationPageLocators.LOGIN_INPUT_EMAIL).send_keys(UserData.current_user.get('email'))
        driver.find_element(AutorizationPageLocators.LOGIN_INPUT_PASSWORD).send_keys(UserData.current_user.get('password'))
        driver.find_element(AutorizationPageLocators.LOG_ON_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
        assert driver.find_element(MainPageLocators.ORDER_BUTTON).text == 'Оформить заказ'

    def test_login_from_registration_page(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MainPageLocators.LK))
        driver.find_element(MainPageLocators.LK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(AutorizationPageLocators.REGISTER))
        driver.find_element(AutorizationPageLocators.REGISTER).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RegistrationPageLocators.LOGIN))
        driver.find_element(RegistrationPageLocators.LOGIN).click()
        driver.find_element(AutorizationPageLocators.LOGIN_INPUT_EMAIL).send_keys(UserData.current_user.get('email'))
        driver.find_element(AutorizationPageLocators.LOGIN_INPUT_PASSWORD).send_keys(UserData.current_user.get('password'))
        driver.find_element(AutorizationPageLocators.LOG_ON_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
        assert driver.find_element(MainPageLocators.ORDER_BUTTON).text == 'Оформить заказ'

    def test_login_from_restore_password_page(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MainPageLocators.LK))
        driver.find_element(MainPageLocators.LK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(AutorizationPageLocators.RESTORE_PASSWORD))
        driver.find_element(MainPageLocators.LK).click(AutorizationPageLocators.RESTORE_PASSWORD)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RegistrationPageLocators.LOGIN))
        driver.find_element(MainPageLocators.LK).click(RegistrationPageLocators.LOGIN)
        driver.find_element(AutorizationPageLocators.LOGIN_INPUT_EMAIL).send_keys(UserData.current_user.get('email'))
        driver.find_element(AutorizationPageLocators.LOGIN_INPUT_PASSWORD).send_keys(UserData.current_user.get('password'))
        driver.find_element(AutorizationPageLocators.LOG_ON_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
        assert driver.find_element(MainPageLocators.ORDER_BUTTON).text == 'Оформить заказ'
