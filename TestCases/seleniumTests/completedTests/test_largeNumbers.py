import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

# this tests large number input verses what the display box shows

# open browser
chromedriver = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
options = Options()
options.headless = True
driver = webdriver.Chrome(chromedriver, options=options)
driver.get("http://localhost:5000")

# begin test
def test_large_numbers():

    #test the display of large numbers
    #input one digit, call back what display box shows, continue loop until it says 'infinity'
    eight_button = driver.find_element_by_xpath("/html/body/main/div/div[2]/div[2]/button")

    for i in range(25):
        eight_button.click()
        # Get the typed value
        displayBox = driver.find_element_by_xpath("/html/body/main/div/div[1]/div").text
        clickReps = i + 1
        #print("8 button clicked " + str(clickReps) + " times, displays " + displayBox)

    # close browser
    driver.quit()

    assert len(displayBox) == clickReps, "Input not displayed accurately"