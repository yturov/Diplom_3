import allure
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators


class OrderFeedPage(BasePage):

    @allure.step("Кликаем на заказ")
    def click_order(self):
        self.wait_element_visibility(OrderFeedLocators.FIRST_ORDER)
        self.find_element(OrderFeedLocators.FIRST_ORDER).click()
        self.wait_element_visibility(OrderFeedLocators.MODAL_WINDOW_ORDER)
        return self.find_element(OrderFeedLocators.MODAL_WINDOW_ORDER)

    @allure.step("Заказы пользователя")
    def order_user(self):
        self.wait_element_visibility(OrderFeedLocators.ALL_ORDERS)
        return self.return_locators_text(OrderFeedLocators.ALL_ORDERS)

    @allure.step("Число выполненных заказов за все время")
    def number_orders_all_time(self):
        self.wait_element_visibility(OrderFeedLocators.COUNTER_ORDER_ALL_TIME)
        return self.get_text(OrderFeedLocators.COUNTER_ORDER_ALL_TIME)

    @allure.step("Число выполненных заказов за сегодня")
    def number_orders_today(self):
        self.wait_element_visibility(OrderFeedLocators.COUNTER_ORDER_TODAY)
        return self.get_text(OrderFeedLocators.COUNTER_ORDER_TODAY)

    @allure.step("Проверяем корзину с готовящимися заказами")
    def check_order_progress_section(self):
        self.wait_element_visibility(OrderFeedLocators.ORDERS_PROGRESS_SECTION)
        return self.return_locators_text(OrderFeedLocators.ORDERS_PROGRESS_SECTION)

    @allure.step("Создаем список всех готовящихся заказов")
    def return_locators_text(self, locator):
        all_locators = self.find_all_element(locator)
        locator_text = []
        for order in all_locators:
            locator_text.append(order.text)
        return locator_text
