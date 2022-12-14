# UNIT-TESTS
# Santiago Garcia Arango, December 2022

import unittest
from solution_1 import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def tests(self):
        self.assertEqual(self.sol.reverse(123), 321)
        self.assertEqual(self.sol.reverse(-123), -321)
        self.assertEqual(self.sol.reverse(120), 21)
        self.assertEqual(self.sol.reverse(123456789), 987654321)
        self.assertEqual(self.sol.reverse(-99999), -99999)
        self.assertEqual(self.sol.reverse(1000000009), 0)
        self.assertEqual(self.sol.reverse(-1000000009), 0)


if __name__ == "__main__":
    unittest.main()
