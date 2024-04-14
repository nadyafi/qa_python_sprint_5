from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import MainPageLocators


class TestConstructor:
    def test_scroll_to_bread(self, driver):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((MainPageLocators.SAUCES)))
        driver.find_element(*MainPageLocators.SAUCES).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((MainPageLocators.BREAD)))
        driver.find_element(*MainPageLocators.BREAD).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((MainPageLocators.BREAD)))
        class_after = driver.find_element(*MainPageLocators.ACTIVE_SECTION_BREAD).get_attribute('class')
        assert 'tab_tab_type_current' in class_after

    def test_scroll_to_sauces(self, driver):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((MainPageLocators.SAUCES)))
        driver.find_element(*MainPageLocators.SAUCES).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((MainPageLocators.SAUCES)))
        class_after = driver.find_element(*MainPageLocators.ACTIVE_SECTION_SAUCES).get_attribute('class')
        assert 'tab_tab_type_current' in class_after

    def test_scroll_to_toppings(self, driver):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((MainPageLocators.TOPPING)))
        driver.find_element(*MainPageLocators.TOPPING).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((MainPageLocators.TOPPING)))
        class_after = driver.find_element(*MainPageLocators.ACTIVE_SECTION_TOPPINGS).get_attribute('class')
        assert 'tab_tab_type_current' in class_after
