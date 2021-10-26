from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObject.VisitPage import VisitPage
from PageObject.SearchFilterBodyStyle import SearchFilterBodyStyle


driver = webdriver.Chrome(executable_path="D:\Selenium\chromedriver.exe")
baseURL = "https://paulcamper.com/rent-camper/"

def set_up():
    driver.get(baseURL)

def test_visitpage():
    VisitPaulCamper = VisitPage(driver)
    VisitPaulCamper.VisitTheURL()

def test_BodyStyleFilter():
    checkCamperbus = SearchFilterBodyStyle(driver)
    checkCamperbus.CheckCamperbus()
    WebDriverWait(driver, 10).until(EC.url_contains("?search"))

def test_BodyStyleBoxVan():
    BoxVan = SearchFilterBodyStyle(driver)
    BoxVan.CheckBoxVan()
    WebDriverWait(driver, 10).until(EC.url_contains("?search"))

def test_BodyStyleAlcoves():
    Alcoves = SearchFilterBodyStyle(driver)
    Alcoves.CheckAlcoves()
    WebDriverWait(driver, 10).until(EC.url_contains("?search"))

def test_BodyStylePartiallyIntegrated():
    Pintergrated = SearchFilterBodyStyle(driver)
    Pintergrated.CheckPartiallyIntegrated()
    WebDriverWait(driver, 10).until(EC.url_contains("?search"))

def test_BodyStyleIntegrated():
    Integrated = SearchFilterBodyStyle(driver)
    Integrated.CheckIntegrated()
    WebDriverWait(driver, 10).until(EC.url_contains("?search"))

def test_BodyStyleCaravan():
    Caravan = SearchFilterBodyStyle(driver)
    Caravan.CheckCaravan()
    WebDriverWait(driver, 10).until(EC.url_contains("?search"))

def test_BodyStyleOther():
    other = SearchFilterBodyStyle(driver)
    other.CheckOther()
    WebDriverWait(driver, 10).until(EC.url_contains("?search"))

#Testcase1 - Filter body type camper bus
set_up()
test_visitpage()
test_BodyStyleFilter()
url = driver.current_url
if "CampingBus" in url:   #verification
    print("Case Passed!! url :" + url)
assert url != baseURL , "Filter Selection Failed"

#Testcase2 - Filter body type Box van
set_up()
test_visitpage()
test_BodyStyleBoxVan()
url = driver.current_url
if "Van" in url:   #verification
    print("Case Passed!! url :" + url)
assert url != baseURL , "Filter Selection Failed"

#Testcase3 - Filter body type Alcoves
set_up()
test_visitpage()
test_BodyStyleAlcoves()
url = driver.current_url
if "Alcove" in url: #verification
    print("Case Passed!! url :" + url)
assert url != baseURL , "Filter Selection Failed"

#Testcase4 - Filter body type Partially integrated
set_up()
test_visitpage()
test_BodyStylePartiallyIntegrated()
url = driver.current_url
if "SemiIntegrated" in url:   #verification
    print("Case Passed!! url :" + url)
assert url != baseURL , "Filter Selection Failed"

#Testcase5 - Filter body type Integrated
set_up()
test_visitpage()
test_BodyStyleIntegrated()
url = driver.current_url
if "Integrated" in url: #verification
    print("Case Passed!! url :" + url)
assert url != baseURL , "Filter Selection Failed"

#Testcase6 - Filter body type Caravan
set_up()
test_visitpage()
test_BodyStyleCaravan()
url = driver.current_url
if "Trailer" in url: #verification
    print("Case Passed!! url :" + url)
assert url != baseURL , "Filter Selection Failed"

#Testcase7 - Filter body type Other
set_up()
test_visitpage()
test_BodyStyleOther()
url = driver.current_url
if "Other" in url: #verification
    print("Case Passed!! url :" + url)
assert url != baseURL , "Filter Selection Failed"

