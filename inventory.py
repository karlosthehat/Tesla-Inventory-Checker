from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
import os
import sys
import http.client, urllib
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(options=options)
link = "https://www.tesla.com/en_AU/inventory/new/my?FleetSalesRegions=QLD%20-%20Gold%20Coast&arrangeby=relevance&zip=2000&range=0"
value = 600 #time in seconds to check for inventory. I recommend 600 to avoid spamming the server

def check_inventory():
    driver.get(link)
    if "no-results-title" in driver.page_source:
        no_results()
    else:
        results()

def no_results():
    print("Nothing found. Checking again in", value, "seconds.")
    time.sleep(value)
    check_inventory()

def results():
    print("Inventory found. Closing “program. Please change your search parameters, update link and restart me.)
    #conn = http.client.HTTPSConnection("api.pushover.net:443")
    #conn.request("POST", "/1/messages.json",
    #    urllib.parse.urlencode({
    #        "token": “xxx”, #put your pushover token here
    #        "user": “xxx”, #put your pushover user code here
    #        "message": "Inventory found. Program closing, to keep searching please change search parameters, update link and restart me.”,
    #        }), { "Content-type": "application/x-www-form-urlencoded" })
    #conn.getresponse()
    driver.quit()
    sys.stdout.flush()
    os._exit(0)

print("Checking inventory....")
check_inventory()
