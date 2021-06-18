from constants import AC_BTN_XPATH, ADD_BTN_XPATH, DISPLAY_BOX_XPATH, DIVIDE_BTN_XPATH, EIGHT_BTN_XPATH, EQUAL_BTN_XPATH, FIVE_BTN_XPATH, MINUS_BTN_XPATH, MULT_BTN_XPATH, NINE_BTN_XPATH, ONE_BTN_XPATH, SEVEN_BTN_XPATH, SIX_BTN_XPATH, THREE_BTN_XPATH, TWO_BTN_XPATH, ZERO_BTN_XPATH
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

    eight_button = driver.find_element_by_xpath(EIGHT_BTN_XPATH)
    add_button = driver.find_element_by_xpath(ADD_BTN_XPATH)
    equal_button = driver.find_element_by_xpath(EQUAL_BTN_XPATH)

    eight_button.click()
    add_button.click()
    eight_button.click()
    equal_button.click()
    result = driver.find_element_by_xpath(DISPLAY_BOX_XPATH).text

    # assert expected results vs actual result
    assert result == "16", "Incorrect answer"

def test_b(): # 8x8=

    # enter '8 x 8 =' expected result '64'

    ac_button = driver.find_element_by_xpath(AC_BTN_XPATH)
    eight_button = driver.find_element_by_xpath(EIGHT_BTN_XPATH)
    mult_button = driver.find_element_by_xpath(MULT_BTN_XPATH)
    equal_button = driver.find_element_by_xpath(EQUAL_BTN_XPATH)

    ac_button.click()
    eight_button.click()
    mult_button.click()
    eight_button.click()
    equal_button.click()
    result = driver.find_element_by_xpath(DISPLAY_BOX_XPATH).text

    # assert expected results vs actual result
    assert result == "64", "Incorrect answer"

def test_c(): # 2-3=

    # enter '2 - 3 =' expected result '-1'

    ac_button = driver.find_element_by_xpath(AC_BTN_XPATH)
    two_button = driver.find_element_by_xpath(TWO_BTN_XPATH)
    minus_button = driver.find_element_by_xpath(MINUS_BTN_XPATH)
    three_button = driver.find_element_by_xpath(THREE_BTN_XPATH)
    equal_button = driver.find_element_by_xpath(EQUAL_BTN_XPATH)

    ac_button.click()
    two_button.click()
    minus_button.click()
    three_button.click()
    equal_button.click()
    result = driver.find_element_by_xpath(DISPLAY_BOX_XPATH).text

    # assert
    assert result == "-1", "Incorrect answer"
    
def test_d(): # 6-9=
    
    # enter '6 - 9 =' , expected answer '-3'

    ac_button = driver.find_element_by_xpath(AC_BTN_XPATH)
    six_button = driver.find_element_by_xpath(SIX_BTN_XPATH)
    minus_button = driver.find_element_by_xpath(MINUS_BTN_XPATH)
    nine_button = driver.find_element_by_xpath(NINE_BTN_XPATH)
    equal_button = driver.find_element_by_xpath(EQUAL_BTN_XPATH)

    ac_button.click()
    six_button.click()
    minus_button.click()
    nine_button.click()
    equal_button.click()
    result = driver.find_element_by_xpath(DISPLAY_BOX_XPATH).text

    # assert
    assert result == '-3', "Incorrect answer"

def test_e(): # 7+7=, 8

    # enter '7 + 7 =' , when answer shows, then enter '8'

    ac_button = driver.find_element_by_xpath(AC_BTN_XPATH)
    seven_button = driver.find_element_by_xpath(SEVEN_BTN_XPATH)
    add_button = driver.find_element_by_xpath(ADD_BTN_XPATH)
    equal_button = driver.find_element_by_xpath(EQUAL_BTN_XPATH)
    eight_button = driver.find_element_by_xpath(EIGHT_BTN_XPATH)

    ac_button.click()
    seven_button.click()
    add_button.click()
    seven_button.click()
    equal_button.click()
    eight_button.click()
    result = driver.find_element_by_xpath(DISPLAY_BOX_XPATH).text

    # assert
    assert result == '8', "Incorrect answer"

def test_f(): # -2=

    # enter ' - 2=', expected answer is '-2'

    ac_button = driver.find_element_by_xpath(AC_BTN_XPATH)
    minus_button = driver.find_element_by_xpath(MINUS_BTN_XPATH)
    two_button = driver.find_element_by_xpath(TWO_BTN_XPATH)
    equal_button = driver.find_element_by_xpath(EQUAL_BTN_XPATH)
    
    ac_button.click()
    minus_button.click()
    two_button.click()
    equal_button.click()
    result = driver.find_element_by_xpath(DISPLAY_BOX_XPATH).text
    
    # assert
    assert result == "-2", "Incorrect answer"

def test_g(): # -2

    # enter ' - 2', expected answer is '-2'

    ac_button = driver.find_element_by_xpath(AC_BTN_XPATH)
    minus_button = driver.find_element_by_xpath(MINUS_BTN_XPATH)
    two_button = driver.find_element_by_xpath(TWO_BTN_XPATH)
    
    ac_button.click()
    minus_button.click()
    two_button.click()
    result = driver.find_element_by_xpath(DISPLAY_BOX_XPATH).text
    
    # assert
    assert result == "-2", "Incorrect answer"

def test_h(): # 10/5=

    # enter '10/5=', expected answer is '2'

    ac_button = driver.find_element_by_xpath(AC_BTN_XPATH)
    zero_button = driver.find_element_by_xpath(ZERO_BTN_XPATH)
    one_button = driver.find_element_by_xpath(ONE_BTN_XPATH)
    five_button = driver.find_element_by_xpath(FIVE_BTN_XPATH)
    divide_button = driver.find_element_by_xpath(DIVIDE_BTN_XPATH)
    equal_button = driver.find_element_by_xpath(EQUAL_BTN_XPATH)

    ac_button.click()
    one_button.click()
    zero_button.click()
    divide_button.click()
    five_button.click()
    equal_button.click()

    result = driver.find_element_by_xpath(DISPLAY_BOX_XPATH).text

    # close browser
    driver.quit()
    
    # assert
    assert result == "2", "Incorrect answer"