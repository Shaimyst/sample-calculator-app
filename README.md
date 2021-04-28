# npm Installs
Package            Version
------------------ -------
pip                21.0.1
pytest             6.2.3
pytest-sugar       0.9.4
python             3.7.3
selenium           3.141.0

# Sample Calculator Application

spin-up with command: `make dev`

navigate to `localhost:5000`

spin-down with mac OS key command: `control+c`

## sequence of commands to run pipenv
install pipenv with: brew install pipenv
setup pipenv virtual-environment for project: pipenv install
spin-up virtual-environment: pipenv shell
do python package installs within virtual-environment ex: pipenv install selenium\
    (puts selenium in the Pipfile)

## instructions for installing chromedriver
install with home brew: brew cask install chromedriver
or using npm: npm install chromedriver

## run all tests through pytest using command 'pytest'
using the command 'pytest' will run all files of the form test_*.py or *_test.py in the current directory and its subdirectories.

### Selenium Tests include:
1. ac button test - confirms AC button returns display to "0"
2. all buttons test - finds all buttons in the app and clicks them. Returns the number of buttons (should be 16). There is a line (commented out) to list which buttons were found and confirms they show up in the display box.
3. button border test - confirms all buttons have a black border
4. button color change test - confirms all buttons change color when clicked
5. buttons test - an accumulation of all individual button tests
6. correct results - tests a multiplication problem and checks the result
7. display box overflow - tests if number run over the display box's border
8. large numbers test - tests the boundaries of inputting large numbers and comparing what is shown in the display box
9. sequences test - multiple tests of indidivual formulas