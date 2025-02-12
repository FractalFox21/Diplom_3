from selenium.webdriver.common.by import By

class LocatorsLoginPage:
    #страница login page
    RECOVER_PASS_BUTTON = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")

class LocatorsForgotPage:
    #страница forgot pass
    EMAIL_INPUT = (By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input")
    RECOVER_BUTTON = (By.XPATH, ".//button[text()='Восстановить']")

class LocatorsPassRecovery:
    # страница pass recovery
    FIELD_PASS = (By.XPATH, '//*[contains(text(),"Пароль")]/parent::*/input')
    SHOW_HIDE_BUTTON = (By.CLASS_NAME, 'input__icon-action')












    #локаторы из спринта
    #домашняя страница
    LOGO = (By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2")  #логотип сайта
    PER_OFFICE = (By.XPATH, ".//p[text()='Личный Кабинет']") #кнопка личного кабинета
    HOME_LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт" на главной странице
    CONSTR = (By.XPATH, ".// p[contains(text(), 'Конструктор')]")  # кнопка конструктор

    #регистрация
    REG_BUTTON = (By.XPATH, './/a[text()="Зарегистрироваться"]')    #кнопка перехода к странице регистрации
    REG_NAME = (By.XPATH, "//label[text()='Имя']/following-sibling::input")    #Поле ввода имени при регистрации
    REG_EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input")  #Поле ввода Email при регистрации
    REG_PASSWORD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")  #Поле ввода пароля при регистрации
    FIN_REG = (By.XPATH, "//button[text()='Зарегистрироваться']") #Кнопка отправки заявки на регистрацию
    REG_ERROR = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]")  # Ошибка некорректного пароля
    ALREADY_REG_INPUT = (By.XPATH, ".//a[contains(text(),'Войти')]") #кнопка "войти" на странице регистрации

    #авторизация
    LOGIN = (By.XPATH, "//label[text()='Email']/following-sibling::input")  #Поле ввода email
    PASSWORD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")   #Поле ввода пароля
    INPUT = (By.XPATH, "//button[contains(text(),'Войти')]")     #Кнопка входа на странице логин
    ORDER = (By.XPATH, ".//button[contains(text(), 'Оформить заказ')]") #Кнопка "оформить заказ" для проверки авторизации
    LOGOUT = (By.XPATH, ".//button[contains(text(),'Выход')]") #Кнопка "выход" из личного кабинета
    RESET_PASS =  (By.XPATH, './/a[text()="Восстановить пароль"]') #кнопка "восстановить пароль" на странице логина
    REMEMBERED_INPUT = (By.XPATH, './/a[text()="Войти"]') #кнопка "войти" на странице восстановления пароля

    #для конструктора
    TOPPINGS = (By.XPATH, ".//span[contains(text(),'Начинки')]")  #пункт меню - начинки
    TEG_TOPPINGS = (By.XPATH, ".//h2[contains(text(),'Начинки')]")  #Раздел меню - начинки
    BUNS = (By.XPATH, ".//span[contains(text(),'Булки')]")      #пункт меню - булки
    TEG_BUNS = (By.XPATH, ".//h2[contains(text(),'Булки')]")    #Раздел меню - булки
    SOUSES = (By.XPATH, ".//span[contains(text(),'Соусы')]")        #пункт меню - соусы
    TEG_SOUSES = (By.XPATH, ".//h2[contains(text(),'Соусы')]")      #Раздел меню - соусы