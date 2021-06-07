import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# this tests difference sequences

# open browser
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://localhost:5000")

# begin test
def test_a(): # 8+8=

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

def test_b(): # 8x8=

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

def test_c(): # 2-3=

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
    
def test_d(): # 6-9=
    
    # enter '6 - 9 =' , expected answer '-3'

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

    # assert
    assert result == '-3', "Incorrect answer"

def test_e(): # 7+7=, 8

    # enter '7 + 7 =' , when answer shows, then enter '8'

    ac_button = driver.find_element_by_xpath("/html/body/main/div/div[4]/div[2]/button")
    seven_button = driver.find_element_by_xpath("/html/body/main/div/div[2]/div[1]/button")
    add_button = driver.find_element_by_xpath("/html/body/main/div/div[3]/div[4]/button")
    equal_button = driver.find_element_by_xpath("/html/body/main/div/div[4]/div[1]/button")
    eight_button = driver.find_element_by_xpath("/html/body/main/div/div[2]/div[2]/button")

    ac_button.click()
    seven_button.click()
    add_button.click()
    seven_button.click()
    equal_button.click()
    eight_button.click()
    result = driver.find_element_by_xpath("/html/body/main/div/div[1]/div").text

    # assert
    assert result == '8', "Incorrect answer"

def test_f(): # -2=

    # enter ' - 2=', expected answer is '-2'

    ac_button = driver.find_element_by_xpath("/html/body/main/div/div[4]/div[2]/button")
    minus_button = driver.find_element_by_xpath("/html/body/main/div/div[3]/div[3]/button")
    two_button = driver.find_element_by_xpath("/html/body/main/div/div[2]/div[8]/button")
    equal_button = driver.find_element_by_xpath("/html/body/main/div/div[4]/div[1]/button")
    
    ac_button.click()
    minus_button.click()
    two_button.click()
    equal_button.click()
    result = driver.find_element_by_xpath("/html/body/main/div/div[1]/div").text
    
    # assert
    assert result == "-2", "Incorrect answer"

def test_g(): # -2

    # enter ' - 2', expected answer is '-2'

    ac_button = driver.find_element_by_xpath("/html/body/main/div/div[4]/div[2]/button")
    minus_button = driver.find_element_by_xpath("/html/body/main/div/div[3]/div[3]/button")
    two_button = driver.find_element_by_xpath("/html/body/main/div/div[2]/div[8]/button")
    
    ac_button.click()
    minus_button.click()
    two_button.click()
    result = driver.find_element_by_xpath("/html/body/main/div/div[1]/div").text
    
    # assert
    assert result == "-2", "Incorrect answer"

def test_h(): # 10/5=

    # enter '10/5=', expected answer is '2'

    ac_button = driver.find_element_by_xpath("/html/body/main/div/div[4]/div[2]/button")
    zero_button = driver.find_element_by_xpath("/html/body/main/div/div[2]/div[10]/button")
    one_button = driver.find_element_by_xpath("/html/body/main/div/div[2]/div[7]/button")
    five_button = driver.find_element_by_xpath("/html/body/main/div/div[2]/div[5]/button")
    divide_button = driver.find_element_by_xpath("/html/body/main/div/div[3]/div[1]/button")
    equal_button = driver.find_element_by_xpath("/html/body/main/div/div[4]/div[1]/button")

    ac_button.click()
    one_button.click()
    zero_button.click()
    divide_button.click()
    five_button.click()
    equal_button.click()

    result = driver.find_element_by_xpath("/html/body/main/div/div[1]/div").text

    # close browser
    driver.quit()
    
    # assert
    assert result == "2", "Incorrect answer"