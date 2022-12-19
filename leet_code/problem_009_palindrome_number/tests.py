# UNIT-TESTS
# Santiago Garcia Arango

import unittest
from solution_1 import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def tests(self):
        self.assertEqual(self.sol.isPalindrome(1234), False)
        self.assertEqual(self.sol.isPalindrome(10), False)
        self.assertEqual(self.sol.isPalindrome(121), True)
        self.assertEqual(self.sol.isPalindrome(-121), False)
        self.assertEqual(self.sol.isPalindrome(0), True)
        self.assertEqual(self.sol.isPalindrome(100001), True)
        self.assertEqual(self.sol.isPalindrome(10001), True)


if __name__ == "__main__":
    unittest.main()
