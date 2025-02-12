from selenium.webdriver.common.by import By

class LocatorsBasePage:
    #кнопка 'личного кабинета'
    PER_OFFICE = (By.XPATH, ".//p[text()='Личный Кабинет']")  # кнопка личного кабинета
    #кнопка 'лента заказов'
    ORDER_LIST = (By.XPATH, '//*[contains(text(),"Лента Заказов")]')
    #кнопка 'конструктор'
    CONSTR = (By.XPATH, ".// p[contains(text(), 'Конструктор')]")

class LocatorsHomePage:
    #найти кнопку булки
    BUN = (By.XPATH, "//*[contains(@alt,'Краторная булка N-200i')]")
    #найти всплывающее окно
    POP_UP_BUN = (By.XPATH, "//h2[text()='Детали ингредиента']")
    #найти кнопку закрытия у всплывающего окна
    EXIT_WINDOW = (By.XPATH, "//*[contains(@class,'Modal_modal__close_modified__3V5XS')]")
    #счётчик ингредиентов
    COUNTER_INGREDIENT = (By.XPATH, '//*[contains(@class,"BurgerIngredient_ingredient__")]//*[contains(@class,"counter_default__")]')
    #место корзины
    PLACE = (By.XPATH, "//span[@class='constructor-element__text' and text()='Перетяните булочку сюда (верх)']")
    #кнопка оформить заказ
    BUTTON_PLACE_ORDER = (By.XPATH, '//button[contains(text(),"Оформить заказ")]')
    #статус каунтера
    CAUNTER_STATUS = (By.XPATH, "//*[contains(@alt, 'Краторная булка N-200i')]/..//*[contains(@class, 'counter_counter__ZNLkj')]")
    # идентификатор заказа для проверки оформления
    ORDER_STATUS = (By.XPATH, '//*[contains(text(),"идентификатор заказа")]')

class LocatorsLoginPage:
    #кнопка восстановить пароль
    RECOVER_PASS_BUTTON = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")
    #поле воода email
    FILED_EMAIL = (By.XPATH, '//*[contains(text(),"Email")]/parent::*/input')
    #поле воода пароля
    FILED_PASSWORD = (By.XPATH, '//*[contains(text(),"Пароль")]/parent::*/input')
    #кнопка войти
    BUTTON_LOGIN = (By.XPATH, '//button[contains(text(),"Войти")]')

class LocatorsForgotPage:
    #поле воода email
    FILED_EMAIL = (By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input")
    # кнопка восстановить
    RECOVER_BUTTON = (By.XPATH, ".//button[text()='Восстановить']")

class LocatorsPassRecovery:
    #поле воода пароля
    FIELD_PASS = (By.XPATH, '//*[contains(text(),"Пароль")]/parent::*/input')
    #иконка показать/скрыть пароль
    SHOW_HIDE_BUTTON = (By.CLASS_NAME, 'input__icon-action')

class LocatorsProfile:
    #кнопка истории заказов
    ORDER_HISTORY_BUTTON = (By.XPATH, "//*[contains(@class,'Account_link__2ETsJ text text_type_main-medium') and text() = 'История заказов']")
    #кнопка выхода
    LOGOUT = (By.XPATH, ".//button[contains(text(),'Выход')]")

class LocatorsProfileOrder:
    #номер заказа в итории для проверки в ленте
    CONTROL_ORDER = (By.XPATH, '//*[contains(@class,"rderHistory_textBox__")]//*[contains(@class,"text_type_digits-default")]')
    #контрольный элемент для окна деталей заказа
    POP_UP_ORDER = (By.XPATH, '//*[contains(@class,"Modal_orderBox")]')
    #количество выполненных за всё время заказов
    ALL_TIME_ORDERS = (By.XPATH, '//*[contains(text(),"Выполнено за все время")]/..//*[contains(@class,"rderFeed_number__")]')
    #количество выполненных за сегодня заказов
    TODAY_ORDERS = (By.XPATH, '//*[contains(text(),"Выполнено за сегодня")]/..//*[contains(@class,"rderFeed_number__")]')
    #номера всех заказов в работе
    ORDERS_IN_WORK = (By.XPATH, "//*[text() = 'В работе:']/following::li[@class][6]")
