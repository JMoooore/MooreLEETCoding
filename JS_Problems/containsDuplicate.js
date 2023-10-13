//Returns true if there is a duplicate in the array of numbers otherwise false
/**
 * @param {number[]} nums
 * @return {boolean}
 */
 var containsDuplicate = function(nums) {
    let distinctNums = {}
    for (let elem of nums) {
        if (distinctNums[elem]) {
            return true
        }
        distinctNums[elem] = 1
    }
    return false
};

//Could use a set instead of an object but it has to convert to a set first which isnt necessarily faster with big arrays
//Could also use map which should be a little bit better on space complexity