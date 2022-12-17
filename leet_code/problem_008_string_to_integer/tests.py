# UNIT-TESTS
# Santiago Garcia Arango

import unittest
from solution_1 import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def tests(self):
        self.assertEqual(self.sol.myAtoi("    -45"), -45)
        self.assertEqual(self.sol.myAtoi("42 45"), 42)
        self.assertEqual(self.sol.myAtoi("4193 with words"), 4193)
        self.assertEqual(self.sol.myAtoi("42++-+-23434"), 42)
        self.assertEqual(self.sol.myAtoi("00000-42a1234"), 0)
        self.assertEqual(self.sol.myAtoi("+5"), 5)
        self.assertEqual(self.sol.myAtoi("   +-55"), 0)
        self.assertEqual(self.sol.myAtoi("+"), 0)
        self.assertEqual(self.sol.myAtoi(""), 0)


if __name__ == "__main__":
    unittest.main()
