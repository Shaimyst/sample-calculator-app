import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

# this test confirms buttons have a black border

# open browser
driver = webdriver.Chrome(ChromeDriverManager().install())
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