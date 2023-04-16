import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH_DRIVER = r'C:\Users\Mathias\Desktop\qa.selenium\chromedriver.exe'

@given(u'launch chrome browser')
def launchBrowser(context):
    options = webdriver.ChromeOptions() 
    # to supress the error messages/logs
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    context.driver = webdriver.Chrome(options=options, executable_path=PATH_DRIVER)

@when(u'open orangehrm homepage')
def openHomePage(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/')
    time.sleep(5)

@then(u'verify that the logo present on page')
def verifyLogo(context):
    logo = context.driver.find_element(By.XPATH, "//img[@alt='company-branding']")
    assert logo.is_displayed() is True

@then(u'close browser')
def closeBrowser(context):
    context.driver.close()