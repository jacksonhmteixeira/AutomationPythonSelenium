import time
from behave import *
from Page.LoginPage import Login

@Given(u'I am on the Login Page')
def login_page(context):
    context.Login = Login()
    context.Login.openBrowserLogin()

@When(u'filling with {email} and {password}')
def fill_email(context, email, password):
    context.Login.fillEmail(email)
    context.Login.fillPassword(password)

@When(u'click the enter button')
def click_enter_button(context):
    context.Login.clickEnterButton()

@Then(u'the system directs you to the home pages')
def check_dashboard_page(context):
    context.Login.verifyPageDashBoard()

@Then(u'the system display the message {errorMessage}')
def system_displays_the_message(context, errorMessage):
    context.Login.verifyErrorMessage(errorMessage)

@Then(u'the system displays the message {emailErrorMessage} and {passwordErrorMessage}')
def system_displays_the_message_error(context, emailErrorMessage, passwordErrorMessage):
    context.Login.verifyRequiredFieldLogin(emailErrorMessage)
    context.Login.verifyRequiredFieldPassWord(passwordErrorMessage)
