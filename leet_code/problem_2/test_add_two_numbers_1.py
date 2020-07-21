# UNIT-TEST FOR <add_two_numbers_1.py>
# Santiago Garcia Arango, July 2020

import unittest
from add_two_numbers_1 import ListNode, Solution


class TestAddTwoNumbers(unittest.TestCase):

    def setUp(self):
        # Create all ListNode objects for the tests
        self.l1 = ListNode(2, ListNode(4, ListNode(3)))
        self.l2 = ListNode(5, ListNode(6, ListNode(4)))
        self.l3 = ListNode(5, ListNode(2))
        self.l4 = ListNode(0)
        self.l5 = ListNode(9, ListNode(9, ListNode(9)))

        self.sol = Solution()

    def tearDown(self):
        pass

    def test_get_full_number(self):
        self.assertEqual(self.sol.get_full_number(self.l1), 342)
        self.assertEqual(self.sol.get_full_number(self.l2), 465)
        self.assertEqual(self.sol.get_full_number(self.l3), 25)
        self.assertEqual(self.sol.get_full_number(self.l4), 0)
        self.assertEqual(self.sol.get_full_number(self.l5), 999)

    def test_add_two_numbers(self):
        result_list_A = self.sol.addTwoNumbers(l1, l2)
        self.assertEqual(result_list_A, )

if __name__ == "__main__":
    unittest.main()
