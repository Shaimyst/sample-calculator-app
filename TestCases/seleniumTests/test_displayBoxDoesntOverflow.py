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

driver.find_element_by_xpath("/html/body/main/div/div[2]/div[2]/button").click()
driver.find_element_by_xpath("/html/body/main/div/div[2]/div[2]/button").click()
driver.find_element_by_xpath("/html/body/main/div/div[2]/div[2]/button").click()
driver.find_element_by_xpath("/html/body/main/div/div[2]/div[2]/button").click()
driver.find_element_by_xpath("/html/body/main/div/div[2]/div[2]/button").click()
driver.find_element_by_xpath("/html/body/main/div/div[2]/div[2]/button").click()
driver.find_element_by_xpath("/html/body/main/div/div[2]/div[2]/button").click()
driver.find_element_by_xpath("/html/body/main/div/div[2]/div[2]/button").click()
driver.find_element_by_xpath("/html/body/main/div/div[2]/div[2]/button").click()

#in case you want to use the display box class, it is "display svelte-1vxpxqz"
displayBox = driver.find_element_by_xpath("/html/body/main/div/div[1]/div").text
print("Test example used is:" + displayBox)

#save screenshot
driver.save_screenshot('/Users/jessicasadler/git/sample-calculator-app/TestCases/seleniumTests/screenshots/screenshot_displayBoxDoesntOverflow.png')

time.sleep(3)

#check box overflow

#close browser
driver.quit()