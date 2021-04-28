import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import time

# this test confirms buttons have a black border

# open browser
chromedriver = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
options = Options()
options.headless = True
driver = webdriver.Chrome(chromedriver, options=options)
driver.get("http://localhost:5000")

# begin test
def test_button_border():

    tags = driver.find_elements_by_tag_name('button')

    for t in tags:
        t.click()
        buttonBorder = t.value_of_css_property("border")
        # print(t.tag_name + " " + t.text + " has a border of " + buttonBorder)

    #close browser
    driver.quit()

    assert buttonBorder == "4px solid rgb(0, 0, 0)", "Border is wrong"