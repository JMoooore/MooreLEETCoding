// Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
// The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
// You must write an algorithm that runs in O(n) time and without using the division operation.

// Example 1:
// Input: nums = [1,2,3,4]
// Output: [24,12,8,6]

// Example 2:
// Input: nums = [-1,1,0,-3,3]
// Output: [0,0,9,0,0]

// Constraints:
//     2 <= nums.length <= 105
//     -30 <= nums[i] <= 30
//     The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

// Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)


//Easy way first
/**
 * @param {number[]} nums
 * @return {number[]}
 */
 var productExceptSelf = function(nums) {
    const product = nums.reduce((prev, curr) => prev * curr)
    nums.map((val, ind) => nums[ind] = product/val)
    return nums
};

//Left multiple and right multiple
//Multiple every value to the left and every value to the right
/**
 * @param {number[]} nums
 * @return {number[]}
 */
 var productExceptSelf = function(nums) {
    const leftArr = []
    const rightArr = []
    let multiple = 1

    for (let i=0; i<nums.length; i++) {
        leftArr[i] = multiple
        multiple *= nums[i]
        //console.log(`leftArr:${leftArr} multiple:${multiple}`)
    }

    multiple=1

    for (let j=nums.length-1; j>=0; j--) {
        rightArr[j] = multiple
        multiple *= nums[j]
        //console.log(`rightArr:${rightArr} multiple:${multiple}`)
        rightArr[j] *= leftArr[j]
    }
    
    return rightArr
};

console.log(productExceptSelf([1,2,3,4]))