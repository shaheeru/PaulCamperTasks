from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
from selenium.webdriver.common.keys import Keys
from PageObject.VisitPage import VisitPage
from PageObject.SearchFilterDistance import SearchFilterDistance
from PageObject.SearchFilterBodyStyle import SearchFilterBodyStyle


driver = webdriver.Chrome(executable_path="D:\Selenium\chromedriver.exe")
baseURL = "https://paulcamper.com/rent-camper/"

def set_up():
    driver.get(baseURL)

def test_visitpage():
    VisitPaulCamper = VisitPage(driver)
    VisitPaulCamper.VisitTheURL()

def test_SearchFilterDistance():
    IncreasedDistance = SearchFilterDistance(driver)
    IncreasedDistance.IncreaseDistance()
    WebDriverWait(driver, 10).until(EC.url_contains("?search"))

def test_BodyStyleAlcoves():
    Alcoves = SearchFilterBodyStyle(driver)
    Alcoves.CheckAlcoves()
    WebDriverWait(driver, 10).until(EC.url_contains("Alcove"))

def test_BodyStyleBoxVan():
    BoxVan = SearchFilterBodyStyle(driver)
    BoxVan.CheckBoxVan()
    WebDriverWait(driver, 10).until(EC.url_contains("Van"))

def test_ResetFilter():
    reset = SearchFilterBodyStyle(driver)
    reset.ResetFilter()

#TestCase - Multiple Filters (2 Body Styles and 1 Distance)
set_up()
test_visitpage()
test_SearchFilterDistance()
test_BodyStyleAlcoves()
test_BodyStyleBoxVan()
filteredurl = driver.current_url

#Verifying by URL if the filters have been applied
if "camper_type=Van" in filteredurl and "camper_type=Alcove" in filteredurl and "max_distance=030" in filteredurl:
    print("Multiple filters passed !! URL :" + filteredurl)
else:
    print("Multiple filters case failed")

#TestCase - Using the reset filter option
test_ResetFilter()
reseturl = driver.current_url

#Verifying if the resetting the filter is successful
if reseturl == filteredurl:
    print("Reset case failed!!")
    if "camper_type=Van" in filteredurl or "camper_type=Alcove" in filteredurl or "max_distance=030" in filteredurl:
        print("Reset case failed!!!!")
else:
    print("reset case Passed !! URL :" + reseturl)

assert reseturl != baseURL, "No changes on the URL - remained same as BaseURL"

