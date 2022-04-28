from behave import *
import time
from Page.MarketPage import Market
from Page.LoginPage import Login
from Page.OpenAndCloseBrowser import OpenAndCloseBrowser

@Given('that I login to check the market page with {email} and {password}')
def that_you_login_to_check_the_market_page(context, email, password):
    context.login = Login()
    context.openAndCloseBrowser = OpenAndCloseBrowser()
    context.login.driverLoginPage(context.openAndCloseBrowser.driverWebdriver())
    context.login.fillEmail(email)
    context.login.fillPassword(password)
    context.login.clickEnterButton()
    context.market = Market()
    context.market.driverMarketPage(context.openAndCloseBrowser.driverWebdriver())

@Given(u'click on the Market Option')
def and_click_on_the_market_option(context):
    context.market.clickMarketButton()

@When(u'click on the Market Option')
def when_click_on_the_market_option(context):
    context.market.clickMarketButton()

@Then('the system directs you to the market pages')
def system_directs_you_to_the_market_pages(context):
    context.market.verifyPageMarket()

@When('the user fills in the search field with {product}')
def the_user_fills_in_the_search_field(context, product):
    context.market.fillProductSearch(product)

@Then('the system displays the searched {product}')
def the_system_displays_the_searched_product(context, product):
    context.market.checkProductPresented(product)
    time.sleep(1)
