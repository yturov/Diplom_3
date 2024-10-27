import allure
from data import Url
from pages.main_functionality import MainFunctionalityPage
from pages.password_recovery_page import PasswordRecoveryPage
from pages.personal_acount_page import PersonalAccountPage


class TestMainFunctionality:

    @allure.title("Переход по клику на «Конструктор»")
    @allure.description("Возможность перехода по кнопке «Конструктор»")
    def test_click_button_construct(self, driver):
        main = MainFunctionalityPage(driver)
        password_recovery = PasswordRecoveryPage(driver)
        password_recovery.click_personal_account()
        assert main.click_constructor_button()

    @allure.title("Переход по клику на «Лента заказов»")
    @allure.description("Возможность перехода на страницу ленты заказов")
    def test_click_button_list_order(self, driver):
        main = MainFunctionalityPage(driver)
        main.click_order_list_button()
        assert main.get_current_url() == Url.FEED_PAGE

    @allure.title("Открытие модального окна при клике на ингредиент")
    @allure.description("При клике на ингредиент, появится всплывающее окно с деталями")
    def test_click_on_ingredient(self, driver):
        main = MainFunctionalityPage(driver)
        assert main.click_ingredient()

    @allure.title("Закрытие модального окна ингредиента")
    @allure.description("Закрытие модального окна кликом на крестик")
    def test_click_close_btn_modal(self, driver):
        main = MainFunctionalityPage(driver)
        main.click_ingredient()
        assert main.click_close_modal_window()

    @allure.title("Добавление ингредиента в заказ")
    @allure.description("Добавлении ингредиента в заказ приводит к увелечению счетчика")
    def test_check_counter_ingredients(self, driver):
        main = MainFunctionalityPage(driver)
        counter = main.add_ingredient_in_order()
        assert int(counter[0]) == 0 and int(counter[1]) == 2

    @allure.title("Авторизованный пользователь оформляет заказ")
    @allure.description("Возможность оформить заказ авторизованным пользователем")
    def test_create_order_authorized_user(self, driver, create_user):
        main = MainFunctionalityPage(driver)
        personal_area = PersonalAccountPage(driver)
        password_recovery = PasswordRecoveryPage(driver)
        password_recovery.click_personal_account()
        personal_area.authorization(create_user)
        main.add_ingredient_in_order()
        assert main.click_create_order()
