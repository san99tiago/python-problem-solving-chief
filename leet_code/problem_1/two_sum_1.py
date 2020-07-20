# SOLUTION 1 OF LEETCODE PROBLEM 1
# Santiago Garcia Arango, July 2020

"""
DESCRIPTION:
Given an array of integers, return indices of the two numbers such that they 
add up to a specific target.

You may assume that each input would have exactly one solution, and you may 
not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                current_sum = nums[i] + nums[j]
                if current_sum == target:
                    return [i, j]


s1 = Solution()
print(s1.twoSum([2, 7, 11, 15], 9))
print(s1.twoSum([2, 3, 5, 6], 9))
