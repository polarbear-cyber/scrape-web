import os
import sqlite3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# adding fodler to the path
os.environ['PATH'] += r"C:\Users\923807\Documents\NACO\GIS\AircraftTransponder"

# adding which browser driver to use
## browser driver can be downloaded in the internet
## to check chrome web driver version to download -> chrome://version
driver = webdriver.Chrome()
options = Options()
options.headless = True

# website to use
driver.get("https://www.flightradar24.com/data/airports/ams/ground")

# wait before clicking
# using implicitly means if the code found the button, it will not wait
# driver.implicityly_wait(10) # time.sleep(10)

# clicking a button
# button = driver.find_element_by_id('downloadButton') # id name in the inspect

# wait button
try:
    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable( # clicking cookie button
            # element filtration
            (By.ID, 'onetrust-accept-btn-handler'),
            # expect to have after X seconds
            # 'Complete!'
        )
    )
    button.click()
except:
    driver.quit ()

driver2 = Chrome(options=options)

def take_tables(table):
    # find all rows within the table
    rows = table.find_elements(By.TAG_NAME, "tr")



    btn = driver.find_element_by_css_selector