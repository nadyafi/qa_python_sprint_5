from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Sprint_5.locators import MainPageLocators


class TestScroll:
    def test_scroll_to_bread(self, driver):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.BREAD))
        driver.find_element(MainPageLocators.SAUCES).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.SAUCES))
        driver.find_element(MainPageLocators.BREAD).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.BREAD))
        assert driver.find_element(MainPageLocators.CURRENT_SECTION).text == 'Булки'

    def test_scroll_to_sauces(self, driver):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.SAUCES))
        driver.find_element(MainPageLocators.SAUCES).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.SAUCES))
        assert driver.find_element(MainPageLocators.CURRENT_SECTION).text == 'Соусы'

    def test_scroll_to_toppings(self, driver):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.TOPPING))
        driver.find_element(MainPageLocators.TOPPING).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.TOPPING))
        assert driver.find_element(MainPageLocators.CURRENT_SECTION).text == 'Начинки'

