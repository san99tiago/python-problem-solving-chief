# LEETCODE PROBLEM 004
# Santiago Garcia Arango, December 2022

"""
4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).


Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_list=[x for n in (nums1, nums2) for x in n]
        merged_list.sort()

        if len(merged_list) % 2 != 0:
            return merged_list[int(len(merged_list)/2)]
        else:
            middle_value = int(len(merged_list)/2) - 1
            return (merged_list[middle_value] + merged_list[middle_value+1])/2
