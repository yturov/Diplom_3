import allure
from pages.password_recovery_page import PasswordRecoveryPage


class TestPasswordRecovery:
    @allure.title("Переход по кнопке «Восстановить пароль»")
    @allure.description("Переход по кнопке «Восстановить пароль»")
    def test_click_on_btn_recovery_page(self, driver):
        password_recovery = PasswordRecoveryPage(driver)
        password_recovery.click_personal_account()
        assert password_recovery.click_recovery_button()

    @allure.title("Ввод почты и нажатие по кнопке «Восстановить»")
    @allure.description("Возможность восстановить пароль по почте")
    def test_input_email_and_click_on_recovery_btn(self, driver):
        password_recovery = PasswordRecoveryPage(driver)
        password_recovery.click_personal_account()
        password_recovery.click_recovery_button()
        assert password_recovery.enter_email_and_click_recovery_button()

    @allure.title("Нажатие по кнопке показать/скрыть пароль делая поле активным")
    @allure.description("Нажатие по иконке глаза приводит к подсветке поля пароля")
    def test_click_password_visible_button(self, driver):
        password_recovery = PasswordRecoveryPage(driver)
        password_recovery.click_personal_account()
        password_recovery.click_recovery_button()
        password_recovery.enter_email_and_click_recovery_button()
        password_recovery.enter_password()
        #assert password_recovery.click_show_hide_password()
