from selenium import webdriver
from PageObject.VisitPage import VisitPage



driver = webdriver.Chrome(executable_path="D:\Selenium\chromedriver.exe")
baseURL = "https://paulcamper.com/rent-camper/"

def set_up():
    driver.get(baseURL)

def test_visitpage():
    VisitPaulCamper = VisitPage(driver)
    VisitPaulCamper.VisitTheURL()


set_up()
test_visitpage()

