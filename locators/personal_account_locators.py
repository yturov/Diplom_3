from selenium.webdriver.common.by import By


class PersonalAccountLocators:
    EMAIL_FIELD = (By.NAME, 'name')  # Поле ввода емейла

    PASSWORD_FIELD = (By.NAME, 'Пароль')  # Поле ввода пароля

    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")  # Кнопка "Войти"

    CREATE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")  # Кнопка "Оформить заказ"

    HISTORY_ORDER_BUTTON = (By.CSS_SELECTOR, 'li.Account_listItem__35dAP:nth-child(2) > a:nth-child(1)')  # Кнопка
    # "История заказов"

    EXIT_BUTTON = (By.CLASS_NAME, 'Account_button__14Yp3')  # Кнопка "Выход"
