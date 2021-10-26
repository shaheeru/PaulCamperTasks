from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
from PageObject.VisitPage import VisitPage
from Common.BrowserSetup import BrowserSetup


class Test_VisitPage(BrowserSetup):

    def __init__(self):
        browserSetup = BrowserSetup()
        browserSetup.set_up()
        #changes

    # driver = webdriver.Chrome(executable_path="D:\Selenium\chromedriver.exe")
    # baseURL = "https://paulcamper.com/rent-camper/"

    # def set_up():
    #     driver.get(baseURL)

    def test_visitpage(self):
        VisitPaulCamper = VisitPage(BrowserSetup.driver)
        VisitPaulCamper.VisitTheURL()


    def test_registerLink(self):
        register = VisitPage(BrowserSetup.driver)
        register.VerifyRegisterTextLink()
        element = BrowserSetup.driver.find_element_by_id("register").get_attribute()
        print(element)
        # assertEqual("register.VerifyRegisterTextLink()", "Register")
        assert element == "Register"


obj = Test_VisitPage()
obj.test_visitpage()
#driver.maximize_window()
#print(driver.current_url)
obj.test_registerLink()
#driver.find_element_by_class_name()