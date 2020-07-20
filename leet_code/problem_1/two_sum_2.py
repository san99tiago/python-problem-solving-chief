# SOLUTION 2 OF LEETCODE PROBLEM 1
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

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        already_checked = {}
        for i in range(len(nums)):
            # Check for complement of the current number in <already_checked>
            complement = target - nums[i]
            if complement in already_checked:
                return [already_checked[complement], i]
            # Add current number checked to the <already_checked> dictionary
            # Note: the value of each key will allow us to return index later
            already_checked[nums[i]] = i

s1 = Solution()
print(s1.twoSum([2, 7, 11, 15], 9))
print(s1.twoSum([2, 3, 5, 6], 9))
