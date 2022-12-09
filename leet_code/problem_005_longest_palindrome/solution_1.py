# LEETCODE PROBLEM 005
# Santiago Garcia Arango, December 2022

"""
5. Longest Palindromic Substring

Given a string s, return the longest 
palindromic substring in s.


Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s), 0, -1):
            for j in range(len(s) - i + 1):
                characters_to_validate = s[j:j+i]
                if characters_to_validate == characters_to_validate[::-1]:
                    return characters_to_validate
