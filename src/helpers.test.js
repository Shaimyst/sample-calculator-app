
import { calcFromParts } from './helpers'


// test helper function (normally a testing lib API method)
const assertEquals = (a, b) => {
    if(a === b) {
        console.log('ok!');
    } else {
        console.log('test FAIL!');
    }
}

// test 1
const result = calcFromParts([1, "+", 1]);
const expected = 2
assertEquals(result, expected)

// test 2
const result2 = calcFromParts([1, "÷", 2])
const expected2 = 0.5;
assertEquals(result2, expected2)

// test 3
const result3 = calcFromParts([3, "×", 3])
const expected3 = 9;
assertEquals(result3, expected3)
