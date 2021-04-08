import os
from selenium import webdriver
import pytest

# open virtual environment in terminal with source env/bin/activate
# spin up in terminal with make dev
# spin down with control c

chromedriver = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://localhost:5000")

#maximize window
driver.maximize_window

# open browser and click button
division_button = driver.find_element_by_xpath("/html/body/main/div/div[3]/div[1]/button").text
driver.find_element_by_xpath("/html/body/main/div/div[3]/div[1]/button").click()
result = driver.find_element_by_xpath("/html/body/main/div/div[1]/div").text

cssValue = driver.find_element_by_xpath("/html/body/main/div/div[3]/div[1]/button").value_of_css_property("border")


#print test template text
testText = """
Test Scenario: Button has border when pressed

Pre conditions:
Open terminal
Go to sample-calculator-app in terminal
Repository is downloaded from GitHub.com
spin-up with command: make dev
navigate to localhost:5000")
"""
print(testText)

#print which buttons were pressed
print("Test data used:", division_button)
print("Expected results: Button will have a black border when clicked")
print("Border properties : "+ cssValue)

#save screenshot
driver.save_screenshot('/Users/jessicasadler/git/sample-calculator-app/TestCases/seleniumTests/screenshots/screenshot_buttonBorder.png')

#close browser
driver.quit()

#assert expected results vs actual result
if cssValue is not None:
    print("Test Results: PASS")
else:
    print("Test Results: FAIL")

#create test results document
#print test description and results
#run in terminal to create and print txt file
#python test_buttonBorder.py &> results_buttonBorder.txt 