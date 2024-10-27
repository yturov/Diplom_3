from selenium.webdriver.common.by import By


class OrderFeedLocators:

    # Первый заказ из списка заказов
    FIRST_ORDER = (By.XPATH, "//div/ul/li[1]")

    # Все заказы
    ALL_ORDERS = (By.XPATH, "//*[contains(@class, 'text text_type_digits-default')]")

    # Счетчик заказов "Выполнено за все время"
    COUNTER_ORDER_ALL_TIME = (By.CSS_SELECTOR, "div.undefined:nth-child(2) > p:nth-child(2)")

    # Счетчик заказов "Выполнено за сегодня"
    COUNTER_ORDER_TODAY = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')

    # Раздел заказов в работе  и готово
    ORDERS_PROGRESS_SECTION = (By.CSS_SELECTOR, "[class='OrderFeed_orderStatusBox__1d4q2 mb-15']")

    # Текст в разделе готовящихся заказов
    ORDERS_PROGRESS_SECTION_TEXT = (By.XPATH, "//*[text() = 'Все текущие заказы готовы!']")

    # Модальное окно заказа с деталями
    MODAL_WINDOW_ORDER = (By.CLASS_NAME, "Modal_orderBox__1xWdi")