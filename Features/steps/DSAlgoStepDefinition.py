from behave import *
from selenium import webdriver

@given('Launch chrome browser')
def LaunchBrowser(context):
    context.driver = webdriver.Chrome(executable_path= "C:\\Users\\HP\\OneDrive\\Desktop\\Shweta\\NUMPY NINJA\\drivers\\chromedriver.exe")


@when('Open DSAlgo page')
def OpenHomePage(context):
    context.driver.get("https://dsportalapp.herokuapp.com/home ")


@then('Varify logo on Home Page')
def VarifyLogo(context):
    status = context.driver.find_element_by_xpath("//a[ text() ='NumpyNinja']").is_displayed()
    assert status is True


@then('Close browser')
def closeBrowser(context):
    context.driver.close()
