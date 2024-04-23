from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import AutorizationPageLocators, MainPageLocators, LkLocators
from User_data import UserData
from URLs import URL


class TestExit:
    def test_exit(self, driver):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((MainPageLocators.LK)))
        driver.find_element(*MainPageLocators.LK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((AutorizationPageLocators.LOG_ON_BUTTON)))
        driver.find_element(*AutorizationPageLocators.LOGIN_INPUT_EMAIL).send_keys(UserData.current_user.get('email'))
        driver.find_element(*AutorizationPageLocators.LOGIN_INPUT_PASSWORD).send_keys(UserData.current_user.get('password'))
        driver.find_element(*AutorizationPageLocators.LOG_ON_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((MainPageLocators.LK)))
        driver.find_element(*MainPageLocators.LK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((LkLocators.EXIT_BUTTON)))
        driver.find_element(*LkLocators.EXIT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((AutorizationPageLocators.LOG_ON_BUTTON)))
        assert (URL.login_page) == driver.current_url
