from behave import *
from selenium import webdriver
@given('I launch chrome browser')
def Launch_Browser(context):
    context.driver = webdriver.Chrome(
        executable_path="C:\\Users\\HP\\OneDrive\\Desktop\\Shweta\\NUMPY NINJA\\drivers\\chromedriver.exe")

@when('I opened DSAlgo home Page')
def Open_Home_Page(context):
    context.driver.get("https://dsportalapp.herokuapp.com/login")

@when(u'Enter Username "{user}" and Password "{pwd}"')
def step_impl(context,user,pwd):
    context.driver.find_element_by_name("username").send_keys(user)
    context.driver.find_element_by_name("password").send_keys(pwd)

@when('click on login button')
def Click_login_button(context):
    context.driver.find_element_by_xpath("//input[@value='Login']").click()

@then('User successfully login')
def Login_successful(context):
    try:
        status = context.driver.find_element_by_xpath("//a[ text() ='NumpyNinja']").is_displayed()
    except:
        context.driver.close()
        assert False,"Test Failed"
    if status == 1:
        context.driver.close()
        assert True, "Test passes"



