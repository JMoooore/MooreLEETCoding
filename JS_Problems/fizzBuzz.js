// Given an integer n, return a string array answer (1-indexed) where:
//     answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
//     answer[i] == "Fizz" if i is divisible by 3.
//     answer[i] == "Buzz" if i is divisible by 5.
//     answer[i] == i (as a string) if none of the above conditions are true.

// Example 1:
// Input: n = 3
// Output: ["1","2","Fizz"]

// Example 2:
// Input: n = 5
// Output: ["1","2","Fizz","4","Buzz"]

// Example 3:
// Input: n = 15
// Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

/**
 * @param {number} n
 * @return {string[]}
 */
//  var fizzBuzz = function(n) {
//     let returnArray = []
    
//     for (let i = 0; i < n; i++) {
//         returnArray[i] = ""
//         if ((i + 1) % 3 === 0) {
//             returnArray[i] += "Fizz"
//         }
//         if ((i + 1) % 5 === 0) {
//             returnArray[i] += "Buzz"
//         }
//         if (returnArray[i] === "") {
//             returnArray[i] += i+1
//         }
//     }
//     return returnArray
// };

var fizzBuzz = function(n) {
    let result = []
    for (let i = 1; i <= n; i++) {
        i % 15 === 0 ? result.push("FizzBuzz") :
        i % 3 === 0 ? result.push("Fizz") :
        i % 5 === 0 ? result.push("Buzz") :
        result.push(""+i)
    }
    return result
}

console.log(fizzBuzz(8))