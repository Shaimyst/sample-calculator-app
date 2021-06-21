import pytest

# this tests all button color changes

# begin test
def test_button_color_change(browserdriver):
    browserdriver.get("http://localhost:5000")

    # loop for finding all buttons and button colors before/after click
    tags = browserdriver.find_elements_by_tag_name('button')

    for t in tags:
        color1 = t.value_of_css_property("background-color")
        t.click()
        color2 = t.value_of_css_property("background-color")
        print("Background colors are:" + color1 + color2)

    # assertion
    assert color1 is not color2, "No color change."