# this test runs all tests for buttons

def test_all_buttons(browserdriver):
    browserdriver.get("http://localhost:5000")
    tags = browserdriver.find_elements_by_tag_name('button')

    count = 0

    for t in tags:
        t.click()
        count += 1 # variable will increment every loop iteration of your code
        tagname = t.tag_name

    # calc should have a 16 buttons have assertion report the correct amount.
    assert count == 16, "There are not 16 buttons"
    assert count > 15, "There are buttons missing"
    assert count < 17, "There are too many buttons"

def test_ac_button(browserdriver):

    # enter test data
    eight_button = browserdriver.find_element_by_xpath("/html/body/main/div/div[2]/div[2]/button")
    ac_button = browserdriver.find_element_by_xpath("/html/body/main/div/div[4]/div[2]/button")

    for i in range(3):
        eight_button.click()

    # Get the typed value
    display1 = browserdriver.find_element_by_xpath("/html/body/main/div/div[1]/div").text

    # press AC button
    ac_button.click()

    # Get the typed value
    display2 = browserdriver.find_element_by_xpath("/html/body/main/div/div[1]/div").text

    # assert display is 0
    assert display2 == str(0), "Display box did not clear!"

def test_button_border(browserdriver):

    tags = browserdriver.find_elements_by_tag_name('button')

    for t in tags:
        t.click()
        buttonBorder = t.value_of_css_property("border")

    assert buttonBorder == "4px solid rgb(0, 0, 0)", "Border is wrong"

def test_button_color_change(browserdriver):

    # loop for finding all buttons and button colors before/after click
    tags = browserdriver.find_elements_by_tag_name('button')

    for t in tags:
        color1 = t.value_of_css_property("background-color")
        t.click()
        color2 = t.value_of_css_property("background-color")

    # assertion
    assert color1 is not color2, "No color change."