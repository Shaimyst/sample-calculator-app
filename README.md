
# Sample Calculator Application

spin-up with command: `make dev`

navigate to `localhost:5000`

spin-down with mac OS key command: `control+c`

## Versions used

Package            Version
------------------ -------
pip                21.0.1
pytest             6.2.3
pytest-sugar       0.9.4
python             3.7.3
selenium           3.141.0

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