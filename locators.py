from selenium.webdriver.common.by import By

class RegistrationPageLocators:  #форма регистрации
    name_input = (By.XPATH, ".//label[text() = 'Имя']/following-sibling::input") #поле ввода имени
    email_input = (By.XPATH, ".//label[text() = 'Email']/following-sibling::input") #поле ввода почты
    password_input = (By.XPATH, ".//label[text() = 'Пароль']/following-sibling::input") #поле ввода пароля
    registration_btn = (By.XPATH, ".//button[text() = 'Зарегистрироваться']") #кнопка Зарегистрироваться
    login_account_btn = (By.XPATH, ".//a[text() = 'Войти']") #кнопка Войти
    error_message_double_registration = (By.XPATH, ".//p[text() = 'Такой пользователь уже существует']") #ошибка при попытке повторной регистрации
    error_message_incorrect_password = (By.XPATH, ".//p[text() = 'Некорректный пароль']") #ошибка при вводе некоррекного пароля
    error_message_registration_name_empty = (By.XPATH, ".//p[text() = 'Заполните поле ИМЯ']") #ошибка при незаполненом поле Имя

class MainPageLocators: #главная страница
    personal_account_btn = (By.XPATH, ".//p[text() = 'Личный Кабинет']") #кнопка личный кабинет
    login_account_btn = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")  #кнопка войти в аккаунт
    place_order_btn = (By.XPATH, ".//button[text() = 'Оформить заказ']") #кнопка оформить заказ
    list_bread = (By.XPATH, ".//span[contains(text(), 'Булки')]") #список булки
    list_sauces = (By.XPATH, ".//span[contains(text(), 'Соусы')]") #список соусы
    list_topping = (By.XPATH, ".//span[contains(text(), 'Начинки')]") #список начинки
    active_list_in_constructor = (By.XPATH, ".//div[contains(@class, 'current')]/span")


class AuthorizationPageLocators: #страница авторизации
    email_input = (By.XPATH, ".//input[@name = 'name']") #поле ввода имени
    password_input = (By.XPATH, ".//input[@name = 'Пароль']") #поле ввода пароля
    login_account_btn = (By.XPATH, "//button[text() = 'Войти']") #кнопка войти

class PersonalAccountLocators: #страница личного кабинета
    exit_btn = (By.XPATH, ".//button[text() = 'Выход']") #кнопка выход
    save_btn = (By.XPATH, ".//button[text() = 'Сохранить']") #кнопка сохранить
    constructor_btn = (By.XPATH, ".//p[text() = 'Конструктор']") #кнопка конструктор
    logo_btn = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']") #кнопка логотип
