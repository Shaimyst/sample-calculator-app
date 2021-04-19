import os
from selenium import webdriver
import pytest

# this test finds and clicks all buttons in the app

chromedriver = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://localhost:5000")

#maximize window
driver.maximize_window

# find all elements of an object using:
# print(dir(t))

tags = driver.find_elements_by_tag_name('button')

count = 0

for t in tags:
    t.click()
    count += 1 # variable will increment every loop iteration of your code
    tagname = t.tag_name
    # option: print list of all buttons clicked
    # print(t.text + " is a " + t.tag_name)

print("There are " + str(count) + " buttons")

#close browser
driver.quit()

# calc should have a 16 buttons have assertion report the correct amount.
assert count == 16, "There are not 16 buttons"
assert count > 15, "There are buttons missing"
assert count < 17, "There are too many buttons"