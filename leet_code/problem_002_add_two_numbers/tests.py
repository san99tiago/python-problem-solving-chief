# UNIT-TEST
# Santiago Garcia Arango, July 2020

import unittest
from solution_1 import ListNode, Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        # Create all ListNode objects for the tests
        self.l1 = ListNode(2, ListNode(4, ListNode(3)))
        self.l2 = ListNode(5, ListNode(6, ListNode(4)))
        self.l3 = ListNode(5, ListNode(2))
        self.l4 = ListNode(0)
        self.l5 = ListNode(9, ListNode(9, ListNode(9)))

        self.sol = Solution()

    def test_get_full_number(self):
        self.assertEqual(self.sol.get_full_number(self.l1), 342)
        self.assertEqual(self.sol.get_full_number(self.l2), 465)
        self.assertEqual(self.sol.get_full_number(self.l3), 25)
        self.assertEqual(self.sol.get_full_number(self.l4), 0)
        self.assertEqual(self.sol.get_full_number(self.l5), 999)

    def test_result_list(self):
        result_list_A = self.sol.result_list("243")
        self.assertEqual(self.sol.get_full_number(result_list_A), 342)

        result_list_B = self.sol.result_list("564")
        self.assertEqual(self.sol.get_full_number(result_list_B), 465)

        result_list_C = self.sol.result_list("52")
        self.assertEqual(self.sol.get_full_number(result_list_C), 25)

        result_list_D = self.sol.result_list("0")
        self.assertEqual(self.sol.get_full_number(result_list_D), 0)

        result_list_E = self.sol.result_list("999")
        self.assertEqual(self.sol.get_full_number(result_list_E), 999)

    def test_add_two_numbers(self):
        result_list_A = self.sol.addTwoNumbers(self.l1, self.l2)
        self.assertEqual(self.sol.get_full_number(result_list_A), 807)

        result_list_B = self.sol.addTwoNumbers(self.l1, self.l3)
        self.assertEqual(self.sol.get_full_number(result_list_B), 367)

        result_list_C = self.sol.addTwoNumbers(self.l2, self.l4)
        self.assertEqual(self.sol.get_full_number(result_list_C), 465)

        result_list_D = self.sol.addTwoNumbers(self.l3, self.l5)
        self.assertEqual(self.sol.get_full_number(result_list_D), 1024)

        result_list_E = self.sol.addTwoNumbers(self.l1, self.l5)
        self.assertEqual(self.sol.get_full_number(result_list_E), 1341)


if __name__ == "__main__":
    unittest.main()
