from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from helpers.locators import Locators
from helpers.urls import Urls

import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Перейти по URL: {url}")
    def navigate_to_url(self, url):
        self.driver.get(url)

    @allure.step("Переключиться на окно {window_number}")
    def switch_to_window(self, window_number, current_url=None, timeout=5):
        self.driver.switch_to.window(self.driver.window_handles[window_number])
        if current_url:
            WebDriverWait(self.driver, timeout).until(EC.url_changes(current_url))

    @allure.step("Дождаться URL: {expected_url}")
    def wait_until_url_matches(self, expected_url, timeout=5):
        WebDriverWait(self.driver, timeout).until(lambda driver: driver.current_url == expected_url)

    @allure.step("Найти элемент: {locator}")
    def find_element(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return self.driver.find_element(*locator)
        except TimeoutException:
            raise NoSuchElementException(f"Элемент с локатором {locator} не найден за {timeout} секунд.")

    @allure.step("Найти все элементы: {locator}")
    def find_elements(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return self.driver.find_elements(*locator)
        except TimeoutException:
            raise NoSuchElementException(f"Элементы с локатором {locator} не найдены за {timeout} секунд.")

    @allure.step("Кликнуть по элементу: {locator}")
    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()

    @allure.step("Получить текст элемента: {locator}")
    def get_element_text(self, locator):
        element = self.find_element(locator)
        return element.text

    @allure.step("Ввести текст '{text}' в элемент: {locator}")
    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Прокрутить страницу до низа")
    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @allure.step("Перетащить элемент {source_locator} в {target_locator}")
    def drag_and_drop(self, source_locator, target_locator, timeout=5):
        source_element = self.find_element(source_locator, timeout)
        target_element = self.find_element(target_locator, timeout)
        action = ActionChains(self.driver)
        action.drag_and_drop(source_element, target_element).perform()

    @allure.step("Дождаться исчезновения элемента: {locator}")
    def wait_until_element_invisible(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step("Дождаться появления элемента: {locator}")
    def wait_until_element_visible(self, locator, time=5):
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Заполнить форму входа: email={email}, password={password}")
    def authorize(self, email, password):
        self.click_element(Locators.PERSONAL_ACCOUNT_BUTTON)
        self.wait_until_url_matches(Urls.PERSONAL_ACCOUNT_URL)
        self.enter_text(Locators.EMAIL_INPUT, email)
        self.enter_text(Locators.PASSWORD_INPUT, password)
        self.click_element(Locators.SIGN_IN_BUTTON)

