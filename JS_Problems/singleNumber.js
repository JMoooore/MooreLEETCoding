//Return digit that isnt repeated

/**
 * @param {number[]} nums
 * @return {number[]}
 */
 var singleNumber = function(nums) {
    const foundNums = {}
    for (let i=0; i<nums.length; i++) {
        if (!foundNums[nums[i]]) {
            foundNums[nums[i]] = 1
        } else {
            delete foundNums[nums[i]]
        }
    }
    return parseInt(Object.keys(foundNums))
};

console.log(findDisappearedNumbers([4,1,2,1,2]))