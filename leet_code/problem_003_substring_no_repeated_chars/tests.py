# UNIT-TESTS
# Santiago Garcia Arango, December 2022

import unittest
from solution_1 import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def tests(self):
        self.assertEqual(self.sol.lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(self.sol.lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(self.sol.lengthOfLongestSubstring("pwwkew"), 3)
        self.assertEqual(self.sol.lengthOfLongestSubstring("abcdef"), 6)


if __name__ == "__main__":
    unittest.main()
