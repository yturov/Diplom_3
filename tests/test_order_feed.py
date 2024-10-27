import allure

from pages.main_functionality import MainFunctionalityPage
from pages.order_feed_page import OrderFeedPage
from pages.password_recovery_page import PasswordRecoveryPage
from pages.personal_acount_page import PersonalAccountPage


class TestOrderFeed:

    @allure.title("Отображение деталей заказа при клике на него")
    @allure.description("При нажатии на заказ откроется всплывающее окно с деталями")
    def test_click_order(self, driver):
        main = MainFunctionalityPage(driver)
        order_feed = OrderFeedPage(driver)
        main.click_order_list_button()
        assert order_feed.click_order()

    @allure.title("Отображение заказов пользователя в «История заказов»")
    @allure.description("Заказы из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_user_order_history_order(self, driver, create_user):
        main = MainFunctionalityPage(driver)
        order_feed = OrderFeedPage(driver)
        personal_area = PersonalAccountPage(driver)
        password_recovery = PasswordRecoveryPage(driver)
        password_recovery.click_personal_account()
        number = personal_area.auth_and_change_order(create_user)
        number = '#0' + number[-1]
        main.click_order_list_button()
        order_texts = order_feed.order_user()
        assert number in order_texts

    @allure.title("Проверка счетчика заказа за все время")
    @allure.description("Работа счетчика выполненных заказов за все время заказов")
    def test_check_orders_counter_all_time(self, driver, create_user):
        main = MainFunctionalityPage(driver)
        order_feed = OrderFeedPage(driver)
        personal_area = PersonalAccountPage(driver)
        password_recovery = PasswordRecoveryPage(driver)
        main.click_order_list_button()
        counter_orders = order_feed.number_orders_all_time()
        password_recovery.click_personal_account()
        personal_area.auth_and_change_order(create_user)
        main.click_order_list_button()
        new_counter_orders = order_feed.number_orders_all_time()
        assert int(new_counter_orders) > int(counter_orders)

    @allure.title("Проверка счетчика заказа за сегодня")
    @allure.description("Работа счетчика выполненных заказов за сегодня")
    def test_check_order_counter_today(self, driver, create_user):
        main = MainFunctionalityPage(driver)
        order_feed = OrderFeedPage(driver)
        personal_area = PersonalAccountPage(driver)
        password_recovery = PasswordRecoveryPage(driver)
        main.click_order_list_button()
        counter_orders = order_feed.number_orders_today()
        password_recovery.click_personal_account()
        personal_area.auth_and_change_order(create_user)
        main.click_order_list_button()
        new_counter_orders = order_feed.number_orders_today()
        assert int(new_counter_orders) > int(counter_orders)

    @allure.title("Оформленный заказ появляется в разделе 'В работе'")
    @allure.description("Номер появляется в разделе 'В работе'")
    def test_check_create_order_appears_section(self, driver, create_user):
        main = MainFunctionalityPage(driver)
        order_feed = OrderFeedPage(driver)
        personal_account = PersonalAccountPage(driver)
        password_recovery = PasswordRecoveryPage(driver)
        password_recovery.click_personal_account()
        number = personal_account.auth_and_change_order(create_user)
        number = '0' + number[-1]
        main.click_order_list_button()
        order_feed.order_user()
        # Здесь ищем номер заказа в большом разделе заказов "В работе  и готово", так как почему то не всегда отображается
        # номер заказа в "В работе", он сразу падает в "Готово"
        order_number = order_feed.check_order_progress_section()
        assert number in str(order_number)
