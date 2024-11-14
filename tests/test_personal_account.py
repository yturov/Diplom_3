import allure
from data import Url
from pages.password_recovery_page import PasswordRecoveryPage
from pages.personal_acount_page import PersonalAccountPage


class TestPersonalAccount:

    @allure.title("Переход по клику на «Личный кабинет»")
    @allure.description("Работа кнопки личного кабинета без выполненной авторизации")
    def test_click_personal_account(self, driver):
        password_recovery = PasswordRecoveryPage(driver)
        password_recovery.click_personal_account()
        assert password_recovery.get_current_url() == Url.AUTHORIZATION_PAGE

    @allure.title("Переход в раздел «История заказов»")
    @allure.description("Открытие страницы истории заказов у авторизованного пользователя")
    def test_click_history_orders(self, driver, create_user):
        password_recovery = PasswordRecoveryPage(driver)
        personal_account = PersonalAccountPage(driver)
        password_recovery.click_personal_account()
        personal_account.authorization(create_user)
        password_recovery.click_personal_account()
        personal_account.open_history_orders()
        assert personal_account.get_current_url() == Url.HISTORY_ORDER_PAGE

    @allure.title("Выход из аккаунта")
    @allure.description("Выход из аккаунта")
    def test_exit(self, driver, create_user):
        password_recovery = PasswordRecoveryPage(driver)
        personal_account = PersonalAccountPage(driver)
        password_recovery.click_personal_account()
        personal_account.authorization(create_user)
        password_recovery.click_personal_account()
        personal_account.logout()
        assert personal_account.get_current_url() == Url.AUTHORIZATION_PAGE
