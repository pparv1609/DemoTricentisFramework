from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    login_link = (By.XPATH,'//a[@href="/login"]')
    email = (By.ID,"Email")
    password = (By.ID,"Password")
    login_btn = (By.XPATH,'//input[@value="Log in"]')


    def login_link_click(self):
        self.click(self.login_link)

    def enter_email(self,email_value):
        self.send_keys(self.email,email_value)
        # self.send_keys(self.email,"abc@gmail.com")

    def enter_password(self,password_value):
        self.send_keys(self.password,password_value)

    def login_btn_click(self):
        self.click(self.login_btn)