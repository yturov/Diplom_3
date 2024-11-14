import allure
from seletools.actions import drag_and_drop
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ищем locator')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Ожидаем что locator появится')
    def wait_element_visibility(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ожидаем когда locator пропадет')
    def wait_not_visibility_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.invisibility_of_element_located(locator))

    @allure.step('Кликаем на locator')
    def click_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Скроллим к locator')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Печатаем text в locator')
    def enter_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Получаем текст из locator')
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step('Ожидаем URL  страницы')
    def wait_url_contains(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_contains(url))
        return self.driver.current_url

    @allure.step('Получаем текущий url')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Ищем все элементы locator')
    def find_all_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(locator))
        return self.driver.find_elements(*locator)

    @allure.step('Перетаскиваем элемент')
    def drag_and_drop(self, point_from, point_where):
        source_element = self.find_element(point_from)
        target_element = self.find_element(point_where)
        drag_and_drop(self.driver, source_element, target_element)
