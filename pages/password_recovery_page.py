import allure
from helpers import generated_data_user
from pages.base_page import BasePage
from locators.password_recovery_locators import PasswordRecoveryLocators


class PasswordRecoveryPage(BasePage):

    @allure.title("Переходим в личный кабинет")
    def click_personal_account(self):
        self.wait_element_visibility(PasswordRecoveryLocators.PERSONAL_ACCOUNT_BUTTON)
        self.click_element(PasswordRecoveryLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.title("Переходим по кнопке 'Восстановить пароль'")
    def click_recovery_button(self):
        self.wait_element_visibility(PasswordRecoveryLocators.RECOVERY_PASSWORD_BUTTON)
        self.click_element(PasswordRecoveryLocators.RECOVERY_PASSWORD_BUTTON)
        return self.find_element(PasswordRecoveryLocators.RECOVERY_PASSWORD_HEADER)

    @allure.title("Вводим email, нажимаем на кнопку 'Восстановить'")
    def enter_email_and_click_recovery_button(self):
        self.wait_element_visibility(PasswordRecoveryLocators.EMAIL_FIELD)
        self.click_element(PasswordRecoveryLocators.EMAIL_FIELD)
        user_data = generated_data_user()
        self.enter_text(PasswordRecoveryLocators.EMAIL_FIELD, user_data['email'])
        self.click_element(PasswordRecoveryLocators.RECOVERY_BUTTON)
        self.wait_element_visibility(PasswordRecoveryLocators.PASSWORD_FIELD)
        return self.find_element(PasswordRecoveryLocators.PASSWORD_FIELD)

    @allure.title("Вводим пароль")
    def enter_password(self):
        self.wait_element_visibility(PasswordRecoveryLocators.PASSWORD_FIELD)
        user_data = generated_data_user()
        self.enter_text(PasswordRecoveryLocators.PASSWORD_FIELD, user_data['password'])

    @allure.step("Клик по кнопке показать/скрыть пароль")
    def click_show_hide_password(self):
        self.wait_element_visibility(PasswordRecoveryLocators.SHOW_HIDE_BUTTON)
        self.click_element(PasswordRecoveryLocators.SHOW_HIDE_BUTTON)
        return self.find_element(PasswordRecoveryLocators.ACTIVE_FIELD)
