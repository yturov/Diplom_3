import allure
from helpers import create_order
from pages.base_page import BasePage
from locators.personal_account_locators import PersonalAccountLocators


class PersonalAccountPage(BasePage):

    @allure.step("Авторизуемся пользователем")
    def authorization(self, create_user):
        user_data, resp = create_user
        self.enter_text(PersonalAccountLocators.EMAIL_FIELD, user_data['email'])
        self.enter_text(PersonalAccountLocators.PASSWORD_FIELD, user_data['password'])
        self.click_element(PersonalAccountLocators.LOGIN_BUTTON)
        self.wait_element_visibility(PersonalAccountLocators.CREATE_ORDER_BUTTON)
        return user_data['email'], user_data['password']

    @allure.step("Авторизоваться и сделать заказ")
    def auth_and_change_order(self, create_user):
        user_data, resp = create_user
        email, password = self.authorization(create_user)
        number = create_order(resp)
        number = str(number.json()['order']['number'])
        return email, password, number

    @allure.title("Вход в историю заказов")
    def open_history_orders(self):
        self.wait_element_visibility(PersonalAccountLocators.HISTORY_ORDER_BUTTON)
        self.click_element(PersonalAccountLocators.HISTORY_ORDER_BUTTON)
        self.wait_element_visibility(PersonalAccountLocators.HISTORY_ORDER_BUTTON)

    @allure.step("Выход из аккаунта")
    def logout(self):
        self.wait_element_visibility(PersonalAccountLocators.EXIT_BUTTON)
        self.click_element(PersonalAccountLocators.EXIT_BUTTON)
        self.wait_element_visibility(PersonalAccountLocators.LOGIN_BUTTON)
