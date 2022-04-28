from behave import *
from Page.LoginPage import Login
from Page.OpenAndCloseBrowser import OpenAndCloseBrowser

@Given(u'I am on the Login Page')
def login_page(context):
    context.login = Login()
    context.openAndCloseBrowser = OpenAndCloseBrowser()
    context.login.driverLoginPage(context.openAndCloseBrowser.driverWebdriver())

@When(u'filling with {email} and {password}')
def fill_email(context, email, password):
    context.login.fillEmail(email)
    context.login.fillPassword(password)

@When(u'click the enter button')
def click_enter_button(context):
    context.login.clickEnterButton()

@Then(u'the system directs you to the home pages')
def check_dashboard_page(context):
    context.login.verifyPageDashBoard()

@Then(u'the system display the message {errorMessage}')
def system_displays_the_message(context, errorMessage):
    context.login.verifyErrorMessage(errorMessage)

@When(u'not filling the required field')
def when_not_filling_the_required_field(context):
    context.login.notFillingTheRequiredField()

@Then(u'the system displays the message {emailErrorMessage} and {passwordErrorMessage}')
def system_displays_the_message_error(context, emailErrorMessage, passwordErrorMessage):
    context.login.verifyRequiredFieldLogin(emailErrorMessage)
    context.login.verifyRequiredFieldPassWord(passwordErrorMessage)
