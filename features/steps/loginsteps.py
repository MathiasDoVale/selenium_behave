import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

PATH_DRIVER = os.environ.get('PATH_DRIVER')

@given(u'I launch chrome browser')
def launchBrowser(context):
    options = webdriver.ChromeOptions() 
    # to supress the error messages/logs
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    context.driver = webdriver.Chrome(options=options, executable_path=PATH_DRIVER)

@when(u'I open orangehrm homepage')
def openHomePage(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/')
    time.sleep(2)

@when('Enter username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.find_element(By.NAME, "username").send_keys(user)
    context.driver.find_element(By.NAME, "password").send_keys(pwd)

@when(u'Click on login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)

@then(u'User must successfully login to the dashboard page')
def step_impl(context):

    try:
        text = context.driver.find_element(By.XPATH, "//h6[text()='Dashboard']").text
    except:
        context.driver.close()
        assert False, "Test failed"

    if text == "Dashboard":
        context.driver.close()
        assert True, "Test passed"
