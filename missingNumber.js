//Return the one missing number from the array of numbers [0,...,n]

/**
 * @param {number[]} nums
 * @return {number}
 */
 var missingNumber = function(nums) {
    let sum = nums.length;
    for (let i = 0; i < nums.length; i++) {
      sum += i - nums[i];
      console.log(`sum:${sum} i:${i} nums:${nums[i]}`)
    }
    return sum;
};

console.log(missingNumber([9,8,4,2,3,5,7,0,1]))

// Add the index and subtract the value in the array
// Start sum at the length because it would be the right next digit in the indexes
// Then the sum at the end is going to be whatever digit wasnt present in the array

