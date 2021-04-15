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

# loop for finding all buttons and printing buttons clicked
# tags = driver.find_elements_by_tag_name('button')

# for t in tags:
#     t.click()
#     print("clicked: " + t.text + " is a " + t.tag_name)

# 7 xpath is /html/body/main/div/div[2]/div[1]/button

# get css value button color
# click
# get color

# return any errors

#close browser
driver.quit()