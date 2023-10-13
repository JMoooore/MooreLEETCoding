// Given an integer array nums of unique elements, return all possible subsets (the power set).
// The solution set must not contain duplicate subsets. Return the solution in any order.

// Example 1:
// Input: nums = [1,2,3]
// Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

// Example 2:
// Input: nums = [0]
// Output: [[],[0]]

// Constraints:
//     1 <= nums.length <= 10
//     -10 <= nums[i] <= 10
//     All the numbers of nums are unique.

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
 var subsets = function(nums) {
    const powerset = [];
	generatePowerset([], 0);

	function generatePowerset(path, index) {
        console.log(powerset)
        console.log(`path:${path} index:${index}`)
		powerset.push(path);
		for (let i = index; i < nums.length; i++) {
			generatePowerset([...path, nums[i]], i + 1);
		}
	}

	return powerset;
};

subsets([1,2,3])

