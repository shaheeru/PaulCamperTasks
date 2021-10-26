from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
from PageObject.Locators import Locator

class SearchFilterBodyStyle():
    def __init__(self,drv):
        self.drv=drv
        self.vehiclefilterbutton = drv.find_element(By.XPATH, Locator.vehicle_filter_button)
        self.box_van_checkbox = drv.find_element(By.XPATH,Locator.box_van_checkbox)

    def CheckCamperbus(self):

        self.vehiclefilterbutton.click()
        self.drv.find_element_by_css_selector('span.checkbox___2AreI').click()
        self.vehiclefilterbutton.click()

    def CheckBoxVan(self):

        #self.vehiclefilterbutton.click()
        self.drv.find_element_by_xpath("//div[@data-test-id='Van']").click()
        self.box_van_checkbox.click()
        self.vehiclefilterbutton.click()

    def CheckAlcoves(self):

        self.vehiclefilterbutton.click()
        self.drv.find_element_by_xpath("//div[@data-test-id='Alcove']").click()
        self.vehiclefilterbutton.click()

    def CheckPartiallyIntegrated(self):
        self.vehiclefilterbutton.click()
        self.drv.find_element_by_xpath("//div[@data-test-id='SemiIntegrated']").click()
        self.vehiclefilterbutton.click()

    def CheckIntegrated(self):
            self.vehiclefilterbutton.click()
            self.drv.find_element_by_xpath("//div[@data-test-id='Integrated']").click()
            self.vehiclefilterbutton.click()

    def CheckCaravan(self):
            self.vehiclefilterbutton.click()
            self.drv.find_element_by_xpath("//div[@data-test-id='Trailer']").click()
            self.vehiclefilterbutton.click()

    def CheckOther(self):
            self.vehiclefilterbutton.click()
            self.drv.find_element_by_xpath("//div[@data-test-id='Other']").click()
            self.vehiclefilterbutton.click()


    def ResetFilter(self):
            self.drv.find_element_by_xpath("//div[@data-test-id='reset-button']").click()
