import os
from selenium import webdriver
import time

# this tests difference sequences

# open browser
chromedriver = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://localhost:5000")

# begin test
def test_a():

    # enter '8 + 8 =' expected result '16'

    eight_button = driver.find_element_by_xpath("/html/body/main/div/div[2]/div[2]/button")
    add_button = driver.find_element_by_xpath("/html/body/main/div/div[3]/div[4]/button")
    equal_button = driver.find_element_by_xpath("/html/body/main/div/div[4]/div[1]/button")

    eight_button.click()
    add_button.click()
    eight_button.click()
    equal_button.click()
    result = driver.find_element_by_xpath("/html/body/main/div/div[1]/div").text

    # assert expected results vs actual result
    assert result == "16", "Incorrect answer"

# begin test
def test_b():

    # enter '8 x 8 =' expected result '64'

    ac_button = driver.find_element_by_xpath("/html/body/main/div/div[4]/div[2]/button")
    eight_button = driver.find_element_by_xpath("/html/body/main/div/div[2]/div[2]/button")
    mult_button = driver.find_element_by_xpath("/html/body/main/div/div[3]/div[2]/button")
    equal_button = driver.find_element_by_xpath("/html/body/main/div/div[4]/div[1]/button")

    ac_button.click()
    eight_button.click()
    mult_button.click()
    eight_button.click()
    equal_button.click()
    result = driver.find_element_by_xpath("/html/body/main/div/div[1]/div").text

    # assert expected results vs actual result
    assert result == "64", "Incorrect answer"

def test_c():

    # enter '2 - 3 =' expected result '-1'

    ac_button = driver.find_element_by_xpath("/html/body/main/div/div[4]/div[2]/button")
    two_button = driver.find_element_by_xpath("/html/body/main/div/div[2]/div[8]/button")
    minus_button = driver.find_element_by_xpath("/html/body/main/div/div[3]/div[3]/button")
    three_button = driver.find_element_by_xpath("/html/body/main/div/div[2]/div[9]/button")
    equal_button = driver.find_element_by_xpath("/html/body/main/div/div[4]/div[1]/button")

    ac_button.click()
    two_button.click()
    minus_button.click()
    three_button.click()
    equal_button.click()
    result = driver.find_element_by_xpath("/html/body/main/div/div[1]/div").text

    # assert
    assert result == "-1", "Incorrect answer"
    
# enter '7 + 7 =' , when answer shows, then enter '5'

# enter '6 - 9 =' , expected answer '-3'
def test_d():
    ac_button = driver.find_element_by_xpath("/html/body/main/div/div[4]/div[2]/button")
    six_button = driver.find_element_by_xpath("/html/body/main/div/div[2]/div[6]/button")
    minus_button = driver.find_element_by_xpath("/html/body/main/div/div[3]/div[3]/button")
    nine_button = driver.find_element_by_xpath("/html/body/main/div/div[2]/div[3]/button")
    equal_button = driver.find_element_by_xpath("/html/body/main/div/div[4]/div[1]/button")

    ac_button.click()
    six_button.click()
    minus_button.click()
    nine_button.click()
    equal_button.click()
    result = driver.find_element_by_xpath("/html/body/main/div/div[1]/div").text

    # close browser
    driver.quit()

    # assert
    assert result == '-3', "Incorrect answer"