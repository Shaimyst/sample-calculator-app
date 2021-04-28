import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# import pytest

# this tests all button color changes

# open browser
chromedriver = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
options = Options()
options.headless = True
driver = webdriver.Chrome(chromedriver, options=options)
driver.get("http://localhost:5000")

# begin test
def test_button_color_change():

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