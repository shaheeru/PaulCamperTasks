from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
from selenium.webdriver.common.keys import Keys
from PageObject.VisitPage import VisitPage
from PageObject.SearchFilterDistance import SearchFilterDistance


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

def test_DecreaseFilterDistance():
    DecreasedDistance = SearchFilterDistance(driver)
    DecreasedDistance.DecreaseDistance()
    WebDriverWait(driver, 10).until(EC.url_contains("?search"))

def test_DistanceFieldValidation():
    validate = SearchFilterDistance(driver)
    validate.CheckDistanceFieldValidation()
    WebDriverWait(driver, 10).until(EC.url_contains("?search"))

set_up()
test_visitpage()
test_SearchFilterDistance()
url = driver.current_url
if "max_distance" in url:
    print("Case Passed!! url :" + url)
assert url != baseURL , "Filter Selection Failed"

set_up()
test_visitpage()
test_SearchFilterDistance()
test_DecreaseFilterDistance()
url = driver.current_url
if "max_distance" in url:
    print("Case Passed!! url :" + url)
assert url != baseURL , "Filter Selection Failed"


#Validating distance filter field by sending Alphabets
set_up()
test_visitpage()
test_DistanceFieldValidation()
url = driver.current_url
if "max_distance=abc" in url:
    print("Case Failed , Distance field can only be in numerics!!" + url)
assert url != baseURL , "Filter Selection Failed"

