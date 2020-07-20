# SOLUTION 1 OF LEETCODE PROBLEM 2
# Santiago Garcia Arango, July 2020

"""
DESCRIPTION:
You are given two non-empty linked lists representing two non-negative 
integers. 
The digits are stored in reverse order and each of their nodes contain a 
single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero,
except the number 0 itself.

Example:
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807
"""

# Definition for singly-linked list. (given by the problem)
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Check that we are given non-null lists
        if self.get_full_number(l1) == 0:
            return l2
        if self.get_full_number(l2) == 0:
            return l1

        # Compute the sum of them and convert them in string
        total = str(self.get_full_number(l1) + self.get_full_number(l2))

        result = self.result_list(total[::-1])
        return result

    def get_full_number(self, list_node):
        # Variable to create string to concatenate numbers of linked lists
        number = ""

        # Current variable to do recurssion on linked_lists until last one
        current = list_node
        while current.next is not None:
            number = str(current.val) + number
            current = current.next
        number = int(str(current.val) + number)
        return number

    def result_list(self, total):
        if len(total) > 0:
            new_total = total[1:]
            return ListNode(int(total[0]), self.result_list(new_total))


l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

sol = Solution()
print("LIST_1 = ", sol.get_full_number(l1))
print("LIST 2 = ", sol.get_full_number(l2))

result_list = sol.addTwoNumbers(l1, l2)
print("RESULT LIST = ", sol.get_full_number(result_list))
