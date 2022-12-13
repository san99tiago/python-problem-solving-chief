# UNIT-TESTS
# Santiago Garcia Arango, December 2022

import unittest
from solution_1 import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def tests(self):
        self.assertEqual(self.sol.convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")
        self.assertEqual(self.sol.convert("PAYPALISHIRING", 4), "PINALSIGYAHRPI")
        self.assertEqual(self.sol.convert("A", 1), "A")
        self.assertEqual(self.sol.convert("SANTIAGOGARCIAARANGO", 3), "SIGIAATAOACARNONGRAG")
        self.assertEqual(self.sol.convert("TOTHEEASTTOTHEWEST", 7), "THOTETOWHTEETSESTA")


if __name__ == "__main__":
    unittest.main()
