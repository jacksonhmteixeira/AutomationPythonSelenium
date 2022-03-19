import time
from behave import *
from Page.Login import Login

@Given(u'I am on the Login Page')
def login_page(context):
    context.Login = Login()
    context.Login.openBrowserLogin()

@When(u'to fill with {email} in the email field')
def fill_email(context, email):
    context.Login.fillEmail(email)

@When(u'to fill with {password} in the password field')
def fill_password(context, password):
    context.Login.fillPassword(password)

@When(u'click the button ENTRAR')
def click_enter_button(context):
    context.Login.clickEnterButton()

@Then(u'the system directs you to the home pages')
def check_dashboard_page(context):
    time.sleep(3)