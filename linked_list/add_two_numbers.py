"""
链表相加

https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1228/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        root = node = ListNode(0)

        while l1 or l2:
            if l1:
                node.val += l1.val
                l1 = l1.next
            if l2:
                node.val += l2.val
                l2 = l2.next
            if node.val > 9:
                node.val -= 10
                node.next = ListNode(1)
                node = node.next
            elif l1 or l2:
                node.next = ListNode(0)
                node = node.next
        return root
