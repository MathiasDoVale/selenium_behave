import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from dotenv.main import load_dotenv
import os

load_dotenv()
PATH_DRIVER = os.environ.get('PATH_DRIVER')

@given(u'launch chrome browser')
def launchBrowser(context):
    print(PATH_DRIVER)
    service = Service(PATH_DRIVER)
    context.driver = webdriver.Chrome(service=service)

@when(u'open orangehrm homepage')
def openHomePage(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/')
    time.sleep(2)

@then(u'verify that the logo present on page')
def verifyLogo(context):
    logo = context.driver.find_element(By.XPATH, "//img[@alt='company-branding']")
    assert logo.is_displayed() is True

@then(u'close browser')
def closeBrowser(context):
    context.driver.close()