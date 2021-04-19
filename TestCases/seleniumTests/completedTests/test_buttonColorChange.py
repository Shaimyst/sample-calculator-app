import os
from selenium import webdriver
import pytest

# this tests all button color changes

chromedriver = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://localhost:5000")

#maximize window
driver.maximize_window

# loop for finding all buttons and button colors before/after click
tags = driver.find_elements_by_tag_name('button')

for t in tags:
    color1 = t.value_of_css_property("background-color")
    t.click()
    color2 = t.value_of_css_property("background-color")
    print("Background colors are:" + color1 + color2)

#close browser
driver.quit()

# assertion
assert color1 is not color2, "No color change."