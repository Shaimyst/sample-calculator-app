import os
from selenium import webdriver
import pytest
import time

# this tests the multiplication function

chromedriver = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://localhost:5000")

#maximize window
driver.maximize_window

# open browser and click '8 x 8 =' expected result '64'

eight_button = driver.find_element_by_xpath("/html/body/main/div/div[2]/div[2]/button").text
mult_button = driver.find_element_by_xpath("/html/body/main/div/div[3]/div[2]/button").text
equal_button = driver.find_element_by_xpath("/html/body/main/div/div[4]/div[1]/button").text

driver.find_element_by_xpath("/html/body/main/div/div[2]/div[2]/button").click()
driver.find_element_by_xpath("/html/body/main/div/div[3]/div[2]/button").click()
driver.find_element_by_xpath("/html/body/main/div/div[2]/div[2]/button").click()
driver.find_element_by_xpath("/html/body/main/div/div[4]/div[1]/button").click()
result = driver.find_element_by_xpath("/html/body/main/div/div[1]/div").text

#print which buttons were pressed
print("Test data used:", eight_button, mult_button, eight_button, equal_button)
print("Expected results: 64")
print("Results given:", result)

#keep browser open for 1 second
time.sleep(1)

#save screenshot
#driver.save_screenshot('/Users/jessicasadler/git/sample-calculator-app/TestCases/seleniumTests/screenshots/screenshot_correctResults.png')

#close browser
driver.quit()

#assert expected results vs actual result
assert result == "64", "FAIL"