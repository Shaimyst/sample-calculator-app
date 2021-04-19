import os
from selenium import webdriver
import pytest

# this tests large number input verses what the display box shows

chromedriver = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://localhost:5000")

#maximize window
driver.maximize_window

#test the display of large numbers
#input one digit, call back what display box shows, continue loop until it says 'infinity'
eight_button = driver.find_element_by_xpath("/html/body/main/div/div[2]/div[2]/button")

for i in range(25):
    eight_button.click()
    # Get the typed value
    displayBox = driver.find_element_by_xpath("/html/body/main/div/div[1]/div").text
    clickReps = i + 1
    print("8 button clicked " + str(clickReps) + " times, displays " + displayBox)

# close browser
driver.quit()

assert len(displayBox) == clickReps, "Input not displayed accurately"