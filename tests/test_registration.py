from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Sprint_5.qa_python_sprint_5.locators import RegistrationPageLocators, AutorizationPageLocators, MainPageLocators
from Sprint_5.User_data import UserData


class TestRegistration:
    def test_success_registration(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MainPageLocators.LK))
        driver.find_element(MainPageLocators.LK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(AutorizationPageLocators.REGISTER))
        driver.find_element(AutorizationPageLocators.REGISTER).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(RegistrationPageLocators.REGISTER_BUTTON))
        driver.find_element(RegistrationPageLocators.REGISTRATION_INPUT_NAME).send_keys(UserData.new_user.get('name'))
        driver.find_element(RegistrationPageLocators.REGISTRATION_INPUT_EMAIL).send_keys(UserData.new_user.get('email'))
        driver.find_element(RegistrationPageLocators.REGISTRATION_INPUT_PASSWORD).send_keys(UserData.new_user.get('password'))
        driver.find_element(RegistrationPageLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(AutorizationPageLocators.LOG_ON_BUTTON))
        assert driver.find_element(AutorizationPageLocators.LOG_ON_BUTTON) == 'Войти'

    def test_registration_with_short_password(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MainPageLocators.LK))
        driver.find_element(MainPageLocators.LK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(AutorizationPageLocators.REGISTER))
        driver.find_element(AutorizationPageLocators.REGISTER).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(RegistrationPageLocators.REGISTER_BUTTON))
        driver.find_element(RegistrationPageLocators.REGISTRATION_INPUT_NAME).send_keys(UserData.new_user.get('name'))
        driver.find_element(RegistrationPageLocators.REGISTRATION_INPUT_EMAIL).send_keys(UserData.new_user.get('email'))
        driver.find_element(RegistrationPageLocators.REGISTRATION_INPUT_PASSWORD).send_keys(UserData.new_user_short_password.get('password'))
        driver.find_element(RegistrationPageLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(RegistrationPageLocators.INCORRECT_PASSWORD_ERROR))
        assert driver.find_element(RegistrationPageLocators.INCORRECT_PASSWORD_ERROR).text == 'Некорректный пароль'
