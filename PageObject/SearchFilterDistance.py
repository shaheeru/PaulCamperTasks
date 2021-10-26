from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
from selenium.webdriver.common.keys import Keys
from PageObject.Locators import Locator

class SearchFilterDistance():

    #VehicleFilter = self.drv.find_element_by_xpath("//span[@data-test-id='FilterCamperType']")

    def __init__(self,drv):
        self.drv=drv
        #self.VehicleFilter = self.drv.find_element_by_xpath("//span[@data-test-id='FilterCamperType']")
        self.vehiclefilterbutton = drv.find_element(By.XPATH,Locator.vehicle_filter_button)
        self.distanceinputfield = drv.find_element(By.XPATH,Locator.distance_input_field)

    def IncreaseDistance(self):
        self.vehiclefilterbutton.click()
        self.distanceinputfield.send_keys("30")
        self.vehiclefilterbutton.click()

    def DecreaseDistance(self):
        self.vehiclefilterbutton.click()
        self.distanceinputfield.send_keys(Keys.CONTROL + "a")
        self.distanceinputfield.send_keys(Keys.DELETE)
        self.distanceinputfield.send_keys("10")
        self.vehiclefilterbutton.click()

    def CheckDistanceFieldValidation(self):
        self.vehiclefilterbutton.click()
        self.distanceinputfield.send_keys(Keys.CONTROL + "a")
        self.distanceinputfield.send_keys(Keys.DELETE)
        self.distanceinputfield.send_keys("abc")
        self.vehiclefilterbutton.click()