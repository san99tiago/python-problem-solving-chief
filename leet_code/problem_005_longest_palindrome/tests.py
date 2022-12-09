# UNIT-TESTS
# Santiago Garcia Arango, December 2022

import unittest
from solution_1 import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def tests(self):
        self.assertEqual(self.sol.longestPalindrome("babad"), "bab")
        self.assertEqual(self.sol.longestPalindrome("cbbd"), "bb")
        self.assertEqual(self.sol.longestPalindrome("santiagoooooooogarciaaa"), "agooooooooga")
        self.assertEqual(self.sol.longestPalindrome("lksdjflksjdflsjkdjflskdjfkjdkfjdkfjdklfsjdkfjlskdjfjfkdsjslkfksjdlflksdjfjsldfsdlfkjslkdjfklsdjfkljfjdkfjkdslfdkjkdjfkjdkfjkdjfkdjfjfffjfjjfjfjfjfjdkfjdkfjdfkjdkdkjsldfjksldfks"), "jfjfffjfj")


if __name__ == "__main__":
    unittest.main()
