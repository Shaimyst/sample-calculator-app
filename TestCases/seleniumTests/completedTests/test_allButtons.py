import os
from selenium import webdriver
import pytest
import time

# open virtual environment in terminal with source env/bin/activate
# spin up in terminal with make dev
# spin down with control c

chromedriver = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://localhost:5000")

#maximize window
driver.maximize_window

# find all elements of an object using:
# print(dir(t))

tags = driver.find_elements_by_tag_name('button')

for t in tags:
    t.click()
    tagname = t.tag_name
    print(t.text + " is a " + t.tag_name)

#close browser
driver.quit()

assert tagname == "button", "Not a button"