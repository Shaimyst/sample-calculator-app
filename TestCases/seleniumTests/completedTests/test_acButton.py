import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import constants

# this test confirms AC button clears the display box

# open browser
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://localhost:5000")

# begin test
def test_ac_button():

    # enter test data
    eight_button = driver.find_element_by_xpath("/html/body/main/div/div[2]/div[2]/button")
    ac_button = driver.find_element_by_xpath("/html/body/main/div/div[4]/div[2]/button")

    for i in range(3):
        eight_button.click()

    # Get the typed value
    display1 = driver.find_element_by_xpath("/html/body/main/div/div[1]/div").text

    # press AC button
    ac_button.click()

    # Get the typed value
    display2 = driver.find_element_by_xpath("/html/body/main/div/div[1]/div").text

    # return what is displayed
    # print("Test data entered: " + display1)
    # print("Data shown after clicking AC button: " + display2)

    # close browser
    driver.quit()

    # assert display is 0
    assert display2 == str(0), "Display box did not clear!"