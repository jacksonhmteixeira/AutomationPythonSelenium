from behave import *
from Page.ProductPage import Product
from Page.LoginPage import Login
from Page.OpenAndCloseBrowser import OpenAndCloseBrowser


@Given(u'that I login to check the product page with {email} and {password}')
def that_I_login_to_check_the_product_page_with_email_and_password(context, email, password):
    context.login = Login()
    context.openAndCloseBrowser = OpenAndCloseBrowser()
    context.login.driverLoginPage(context.openAndCloseBrowser.driverWebdriver())
    context.login.fillEmail(email)
    context.login.fillPassword(password)
    context.login.clickEnterButton()
    context.product = Product()
    context.product.driverProductPage(context.openAndCloseBrowser.driverWebdriver())

@When(u'click on the Product Option')
def click_on_the_page_product_option(context):
    context.product.clickProductButton()

@Then(u'the system directs you to the product pages')
def the_system_directs_you_to_the_product_pages(context):
    context.product.verifyPageProduct()