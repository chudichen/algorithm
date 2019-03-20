# -*- coding: utf-8 -*-
"""
https://leetcode.com/explore/featured/card/recursion-i/251/scenario-i-recurrence-relation/2378/
解题思路将使用虚拟before指针，将head的值依次传递给before，最终形成反转链表。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def reverse_list(self, head: ListNode) -> ListNode:
        before = None
        while head:
            temp = head.next
            head.next = before
            before = head
            head = temp
        return before


# 测试方法
if __name__ == '__main__':
    headNode = ListNode(1)
    add = headNode
    for i in range(2, 6):
        add.next = ListNode(i)
        add = add.next

    solution = Solution()
    solution.reverse_list(headNode)

