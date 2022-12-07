# LEETCODE PROBLEM 003
# Santiago Garcia Arango, December 2022

"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest 
substring without repeating characters.


Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_string = ""
        max_size = 0
        for i in range(len(s)):
            if s[i] in current_string:
                current_string = "{}{}".format(current_string.split(s[i])[1], s[i])
            else:
                current_string = "{}{}".format(current_string, s[i])
                if max_size < len(current_string):
                    max_size = len(current_string)
        return max_size
