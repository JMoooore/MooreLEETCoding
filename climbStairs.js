/**
 * @param {number} n
 * @return {number}
 */
 var climbStairs = function(n) {
    let firstDigit = 1
    let lastDigit = 1
    let temp
    for (let i = 1; i<n; i++)  {
        console.log(`i:${i} lastDigit:${lastDigit}`)
        temp = lastDigit
        lastDigit += firstDigit
        firstDigit = temp
    }
    return lastDigit
  };

  console.log(climbStairs(5))