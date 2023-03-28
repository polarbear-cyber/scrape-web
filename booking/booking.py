import booking.constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Booking(webdriver.Chrome):
    def __init__(self, driver_path = r"C:\Users\923807\Documents\NACO\GIS\AircraftTransponder", teardown=False): #driver_path
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def launchBrowser(self):
        self.get(const.BASE_URL)
        while(True):
            pass
    
    def acceptCookie(self):
        cookie = self.find_element(
            By.ID,
            "onetrust-accept-btn-handler"
        )
        cookie.click()

    def changeCurrency(self, currency=None):
        currencyOption = self.find_element(
            By.CSS_SELECTOR,
            'button[data-testid="header-currency-picker-trigger"]'
            )
        currency.click()
        selectedCurrency = self.find_element(
            By.CSS_SELECTOR,
            'a.data-modal-header-async-url-param*="selected_currency={currency}"'
        )
        selectedCurrency.click()

    def placeStay(self, stay)
        search_field = self.find_element(
            By.ID,
            'ss'
        )
        search_field.clear()
        search_field.send_keys(stay)

        first_result = self.find_element(
            By.CSS_SELECTOR,
            'li.data-i="0"'
        )
        first_result.click()
    
    def dateStay(self, check_in, check_out):
        check_in = self.find_element(
            By.CSS_SELECTOR,
            f'td.data-date="{check_in}"'
        )
        check_in.click()

        check_out = self.find_element(
            By.CSS_SELECTOR,
            f'td.data-date="{check_out}"'
        )
        check_out.click()

    def numberPeople(self, adult, children, room):
        number = self.find_element(
            By.ID,
            '###'
        )
        number.click()
        
        whilte True:
            decreaseAdult = self.find_element(
                By.CSS_SELECTOR,
                '###'
            )
            decreaseAdult.click() #if the value is == 1. quit
            adultValue = self.find_element(
                By.ID,
                'group_adults'
            )
            adultValue.get_attribute('value') # Should give back the adults count

            if int(adultValue) == 1:
                break
        
        increaseAdult = self.find_element(
            By.CSS_SELECTOR,
            'button.aria-label.Increase number of Adults'
        )
        
        for i in range(count - 1):
            increaseAdult.click()

    def submitSearch(self):
        self.find_element(
            By.CSS_SELECTOR,
            'button.type=submit'
        )
        submitSearch.click()