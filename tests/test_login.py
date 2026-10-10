from pages.login_page import LoginPage


## using normal way

'''def test_login(setup_and_teardown):
    lg = LoginPage(setup_and_teardown)
    lg.login_link_click()
    lg.enter_email("hello.12@gmail.com")
    lg.enter_password("123456")
    lg.login_btn_click()
'''


### Using Data Driven Testing
import pytest
from utilities.read_excle import get_login_data

@pytest.mark.parametrize("email,password",get_login_data())
def test_login(setup_and_teardown,email,password):
    lg = LoginPage(setup_and_teardown)
    lg.login_link_click()
    lg.enter_email(email)
    lg.enter_password(password)
    lg.login_btn_click()