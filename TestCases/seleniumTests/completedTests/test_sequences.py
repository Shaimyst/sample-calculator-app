import constants as c

# this tests difference sequences

def test_a(browserdriver): # 8+8=
    # enter '8 + 8 =' expected result '16'

    browserdriver.get("http://localhost:5000")

    eight_button = browserdriver.find_element_by_xpath(c.EIGHT_BTN_XPATH)
    add_button = browserdriver.find_element_by_xpath(c.ADD_BTN_XPATH)
    equal_button = browserdriver.find_element_by_xpath(c.EQUAL_BTN_XPATH)

    eight_button.click()
    add_button.click()
    eight_button.click()
    equal_button.click()
    result = browserdriver.find_element_by_xpath(c.DISPLAY_BOX_XPATH).text

    # assert expected results vs actual result
    assert result == "16", "Incorrect answer"

def test_b(browserdriver): # 8x8=

    # enter '8 x 8 =' expected result '64'

    ac_button = browserdriver.find_element_by_xpath(c.AC_BTN_XPATH)
    eight_button = browserdriver.find_element_by_xpath(c.EIGHT_BTN_XPATH)
    mult_button = browserdriver.find_element_by_xpath(c.MULT_BTN_XPATH)
    equal_button = browserdriver.find_element_by_xpath(c.EQUAL_BTN_XPATH)

    ac_button.click()
    eight_button.click()
    mult_button.click()
    eight_button.click()
    equal_button.click()
    result = browserdriver.find_element_by_xpath(c.DISPLAY_BOX_XPATH).text

    # assert expected results vs actual result
    assert result == "64", "Incorrect answer"

def test_c(browserdriver): # 2-3=

    # enter '2 - 3 =' expected result '-1'

    ac_button = browserdriver.find_element_by_xpath(c.AC_BTN_XPATH)
    two_button = browserdriver.find_element_by_xpath(c.TWO_BTN_XPATH)
    minus_button = browserdriver.find_element_by_xpath(c.MINUS_BTN_XPATH)
    three_button = browserdriver.find_element_by_xpath(c.THREE_BTN_XPATH)
    equal_button = browserdriver.find_element_by_xpath(c.EQUAL_BTN_XPATH)

    ac_button.click()
    two_button.click()
    minus_button.click()
    three_button.click()
    equal_button.click()
    result = browserdriver.find_element_by_xpath(c.DISPLAY_BOX_XPATH).text

    # assert
    assert result == "-1", "Incorrect answer"
    
def test_d(browserdriver): # 6-9=
    
    # enter '6 - 9 =' , expected answer '-3'

    ac_button = browserdriver.find_element_by_xpath(c.AC_BTN_XPATH)
    six_button = browserdriver.find_element_by_xpath(c.SIX_BTN_XPATH)
    minus_button = browserdriver.find_element_by_xpath(c.MINUS_BTN_XPATH)
    nine_button = browserdriver.find_element_by_xpath(c.NINE_BTN_XPATH)
    equal_button = browserdriver.find_element_by_xpath(c.EQUAL_BTN_XPATH)

    ac_button.click()
    six_button.click()
    minus_button.click()
    nine_button.click()
    equal_button.click()
    result = browserdriver.find_element_by_xpath(c.DISPLAY_BOX_XPATH).text

    # assert
    assert result == '-3', "Incorrect answer"

def test_e(browserdriver): # 7+7=, 8

    # enter '7 + 7 =' , when answer shows, then enter '8'

    ac_button = browserdriver.find_element_by_xpath(c.AC_BTN_XPATH)
    seven_button = browserdriver.find_element_by_xpath(c.SEVEN_BTN_XPATH)
    add_button = browserdriver.find_element_by_xpath(c.ADD_BTN_XPATH)
    equal_button = browserdriver.find_element_by_xpath(c.EQUAL_BTN_XPATH)
    eight_button = browserdriver.find_element_by_xpath(c.EIGHT_BTN_XPATH)

    ac_button.click()
    seven_button.click()
    add_button.click()
    seven_button.click()
    equal_button.click()
    eight_button.click()
    result = browserdriver.find_element_by_xpath(c.DISPLAY_BOX_XPATH).text

    # assert
    assert result == '8', "Incorrect answer"

def test_f(browserdriver): # -2=

    # enter ' - 2=', expected answer is '-2'

    ac_button = browserdriver.find_element_by_xpath(c.AC_BTN_XPATH)
    minus_button = browserdriver.find_element_by_xpath(c.MINUS_BTN_XPATH)
    two_button = browserdriver.find_element_by_xpath(c.TWO_BTN_XPATH)
    equal_button = browserdriver.find_element_by_xpath(c.EQUAL_BTN_XPATH)
    
    ac_button.click()
    minus_button.click()
    two_button.click()
    equal_button.click()
    result = browserdriver.find_element_by_xpath(c.DISPLAY_BOX_XPATH).text
    
    # assert
    assert result == "-2", "Incorrect answer"

def test_g(browserdriver): # -2

    # enter ' - 2', expected answer is '-2'

    ac_button = browserdriver.find_element_by_xpath(c.AC_BTN_XPATH)
    minus_button = browserdriver.find_element_by_xpath(c.MINUS_BTN_XPATH)
    two_button = browserdriver.find_element_by_xpath(c.TWO_BTN_XPATH)
    
    ac_button.click()
    minus_button.click()
    two_button.click()
    result = browserdriver.find_element_by_xpath(c.DISPLAY_BOX_XPATH).text
    
    # assert
    assert result == "-2", "Incorrect answer"

def test_h(browserdriver): # 10/5=

    # enter '10/5=', expected answer is '2'

    ac_button = browserdriver.find_element_by_xpath(c.AC_BTN_XPATH)
    zero_button = browserdriver.find_element_by_xpath(c.ZERO_BTN_XPATH)
    one_button = browserdriver.find_element_by_xpath(c.ONE_BTN_XPATH)
    five_button = browserdriver.find_element_by_xpath(c.FIVE_BTN_XPATH)
    divide_button = browserdriver.find_element_by_xpath(c.DIVIDE_BTN_XPATH)
    equal_button = browserdriver.find_element_by_xpath(c.EQUAL_BTN_XPATH)

    ac_button.click()
    one_button.click()
    zero_button.click()
    divide_button.click()
    five_button.click()
    equal_button.click()

    result = browserdriver.find_element_by_xpath(c.DISPLAY_BOX_XPATH).text
    
    # assert
    assert result == "2", "Incorrect answer"