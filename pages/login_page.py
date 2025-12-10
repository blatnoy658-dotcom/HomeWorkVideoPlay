from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.phone_input = (By.CSS_SELECTOR, "#app > div > div > div > div.log-in__container > div > div.log-in__newContent-right > div > div.log-in__newContent-right-block-wrap > form > div.log-in__newContent-right-block-center > div > label")
        self.btn_next = (By.CSS_SELECTOR, "#app > div > div > div > div.log-in__container > div > div.log-in__newContent-right > div > div.log-in__newContent-right-block-wrap > form > div.log-in__newContent-right-block-bot > button")
        self.password = (By.CSS_SELECTOR, "#app > div > div > div > div.log-in__container > div > div.log-in__newContent-right > div > div.log-in__newContent-right-block-wrap > form > div.log-in__newContent-right-block-center.log-in__newContent-right-block-center-checkpass > div.log-in__newContent-right-block-center-inp > label")
        self.btn_submit = (By.CSS_SELECTOR, "#app > div > div > div > div.log-in__container > div > div.log-in__newContent-right > div > div.log-in__newContent-right-block-wrap > form > div.log-in__newContent-right-block-bot > button")
        self.btn_sessions = (By.CSS_SELECTOR, "#dialog > div > div > div > div.material-dialog__window-body.material-dialog__window-body_modify > div > div:nth-child(2) > div")
        self.btn_finish = (By.CSS_SELECTOR, "#dialog > div > div > div > div.material-dialog__window-body.material-dialog__window-body_modify > div > div:nth-child(2) > div.drop-down-component__content > div.sessions__item-content > button")

    def enter_phone_input(self, phone_input):
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_element_located(self.phone_input)).send_keys(phone_input)

    def click_btn_next(self):
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.element_to_be_clickable(self.btn_next)).click()

    def enter_password(self, password):
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_element_located(self.password)).send_keys(password)

    def click_btn_submit(self):
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.element_to_be_clickable(self.btn_submit)).click()

    def click_btn_sessions(self):
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.element_to_be_clickable(self.btn_sessions)).click()

    def click_btn_finish(self):
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.element_to_be_clickable(self.btn_finish)).click()