# UNIT-TESTS
# Santiago Garcia Arango, July 2020

import unittest
from solution_1 import Solution
# from solution_2 import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sums(self):
        self.assertEqual(self.sol.twoSum([1, 2, 3], 5), [1, 2])
        self.assertEqual(self.sol.twoSum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(self.sol.twoSum([2, 3, 5, 6], 9), [1, 3])
        self.assertEqual(self.sol.twoSum([4, 5, 2, 7, 8, 3], 13), [1, 4])


if __name__ == "__main__":
    unittest.main()
