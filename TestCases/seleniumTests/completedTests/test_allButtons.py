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

# clicking loop
like = driver.find_elements_by_class_name("svelte-1wpgx6i")
for x in range(0,len(like)):
    if like[x].is_displayed():
        like[x].click()

# optional: list all buttons pressed
# return any errors

#close browser
driver.quit()