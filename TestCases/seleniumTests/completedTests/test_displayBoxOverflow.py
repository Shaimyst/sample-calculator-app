import os
from selenium import webdriver
import pytest

# this tests if input runs outside the display box

chromedriver = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://localhost:5000")

# enter test data
# Type more than 8 characters as max limit should be 8

eight_button = driver.find_element_by_xpath("/html/body/main/div/div[2]/div[2]/button")

for i in range(12):
    eight_button.click()

# Get the typed value
displayBox = driver.find_element_by_xpath("/html/body/main/div/div[1]/div").text
# displayBox = driver.find_element_by_class_name("svelte-1eg8bj3").text
print("Test data used:" + displayBox)
print("The length is:", len(displayBox))

# save screenshot
driver.save_screenshot('/Users/jessicasadler/git/sample-calculator-app/TestCases/seleniumTests/screenshots/screenshot_displayBoxDoesntOverflow.png')

# close browser
driver.quit()

# assertion
assert len(displayBox) <= 8, "Text overflows display box"