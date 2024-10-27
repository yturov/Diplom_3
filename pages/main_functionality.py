import allure
from pages.base_page import BasePage
from locators.main_functionality_locators import MainFunctionalityLocators


class MainFunctionalityPage(BasePage):

    @allure.step("Нажимаем на кнопку «Конструктор»")
    def click_constructor_button(self):
        self.wait_element_visibility(MainFunctionalityLocators.CONSTRUCTOR_BUTTON)
        self.click_element(MainFunctionalityLocators.CONSTRUCTOR_BUTTON)
        return self.find_element(MainFunctionalityLocators.CONSTRUCTOR_TITLE)

    @allure.step("Нажимаем на кнопку «Лента заказов»")
    def click_order_list_button(self):
        self.wait_element_visibility(MainFunctionalityLocators.ORDER_LIST_BUTTON)
        self.click_element(MainFunctionalityLocators.ORDER_LIST_BUTTON)
        return self.get_current_url()

    @allure.step("Нажимаем на ингрeдиент на главной странице")
    def click_ingredient(self):
        self.click_element(MainFunctionalityLocators.BUN)
        self.wait_element_visibility(MainFunctionalityLocators.MODAL_WINDOW_INGREDIENT)
        return self.find_element(MainFunctionalityLocators.MODAL_WINDOW_INGREDIENT)

    @allure.step("Нажимаем на кнопку закрытия модального окна")
    def click_close_modal_window(self):
        self.click_element(MainFunctionalityLocators.CLOSE_BUTTON_MODAL_WINDOW)
        self.wait_not_visibility_element(MainFunctionalityLocators.CLOSE_BUTTON_MODAL_WINDOW)
        return self.find_element(MainFunctionalityLocators.CLOSE_BUTTON_MODAL_WINDOW)

    @allure.step("Добавить ингредиент в заказ")
    def add_ingredient_in_order(self):
        self.wait_element_visibility(MainFunctionalityLocators.COUNTER_BUN)
        counter = self.get_text(MainFunctionalityLocators.COUNTER_BUN)
        self.drag_and_drop(MainFunctionalityLocators.BUN, MainFunctionalityLocators.BASKET_INGREDIENT)
        new_counter = self.get_text(MainFunctionalityLocators.COUNTER_BUN)
        return counter, new_counter

    @allure.step("Кликаем на кнопку «Оформить заказ»")
    def click_create_order(self):
        self.wait_element_visibility(MainFunctionalityLocators.CREATE_ORDER_BUTTON)
        self.click_element(MainFunctionalityLocators.CREATE_ORDER_BUTTON)
        self.wait_element_visibility(MainFunctionalityLocators.CREATE_ORDER_MODAL_WINDOW)
        return self.find_element(MainFunctionalityLocators.CREATE_ORDER_MODAL_WINDOW)