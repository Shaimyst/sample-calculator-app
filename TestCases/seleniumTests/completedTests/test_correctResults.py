import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

# this tests the multiplication function

# open browser
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://localhost:5000")

# begin test
def test_correct_results():

    # enter '8 x 8 =' expected result '64'

    eight_button = driver.find_element_by_xpath("/html/body/main/div/div[2]/div[2]/button")
    mult_button = driver.find_element_by_xpath("/html/body/main/div/div[3]/div[2]/button")
    equal_button = driver.find_element_by_xpath("/html/body/main/div/div[4]/div[1]/button")

    eight_button.click()
    mult_button.click()
    eight_button.click()
    equal_button.click()
    result = driver.find_element_by_xpath("/html/body/main/div/div[1]/div").text

    #close browser
    driver.quit()

    #assert expected results vs actual result
    assert result == "64", "FAIL"