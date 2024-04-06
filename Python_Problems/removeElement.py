from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # use the two pointer method
        # left pointer starts at 0
        # right pointer starts at -1
        # as long as left pointer is pointing at value (iterate if so)
        # swap left w/ right every time left is equal to value
        # return left -1 if doing a while left < right
        count = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        return count

if __name__ == '__main__':
    solution = Solution()
    solution.removeElement(nums=[3,2,2,3], val=3)