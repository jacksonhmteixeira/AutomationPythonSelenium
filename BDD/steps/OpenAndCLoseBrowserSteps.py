from behave import *
from Page.OpenAndCloseBrowser import OpenAndCloseBrowser

@Given(u'I open the browser')
def i_open_the_browser(context):
    context.openAndCloseBrowser = OpenAndCloseBrowser()
    context.openAndCloseBrowser.openBrowser()

@Given(u'I want to close the browser')
def i_want_to_open_the_browser(context):
    pass

@Then(u'I close the browser')
def i_open_the_browser(context):
    context.openAndCloseBrowser.closeBrowser()


