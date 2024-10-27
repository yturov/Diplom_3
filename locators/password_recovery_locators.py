from selenium.webdriver.common.by import By


class PasswordRecoveryLocators:
    # Кнопка "Личный Кабинет"
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")

    # Кнопка "Восстановить пароль"
    RECOVERY_PASSWORD_BUTTON = (By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Восстановить пароль']")

    # Текст заголовка страницы "Восстановления пароля"
    RECOVERY_PASSWORD_HEADER = (By.XPATH, "//h2[text()='Восстановление пароля']")

    # Кнопка "Восстановить"
    RECOVERY_BUTTON = (By.XPATH, "//button[text()='Восстановить']")

    # Поле ввода password
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")

    # Поле ввода email
    EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/../input")

    # Кнопка показать/скрыть пароль
    SHOW_HIDE_BUTTON = (By.CSS_SELECTOR, ".input__icon > svg:nth-child(1)")

    # Активное поле
    ACTIVE_FIELD = (By.XPATH, "//div[contains(@class, 'input_status_active')]")
