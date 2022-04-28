from behave import *
from Page.MarketPage import Market
from Page.LoginPage import Login
from Page.OpenAndCloseBrowser import OpenAndCloseBrowser

@Given(u'that you login to check the market page with {email} and {password}')
def that_you_login_to_check_the_market_page(context, email, password):
    context.login = Login()
    context.openAndCloseBrowser = OpenAndCloseBrowser()
    context.login.driverLoginPage(context.openAndCloseBrowser.driverWebdriver())
    context.login.fillEmail(email)
    context.login.fillPassword(password)
    context.login.clickEnterButton()
    context.market = Market()
    context.market.driverMarketPage(context.openAndCloseBrowser.driverWebdriver())

@When(u'click on the Market Option')
def click_on_the_market_option(context):
    context.market.clickMarketButton()

@Then(u'the system directs you to the market pages')
def system_directs_you_to_the_market_pages(context):
    context.market.verifyPageMarket()