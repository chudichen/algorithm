# -*- coding: utf-8 -*-
"""
反转相邻的两对

解题思路创建三个临时指针，将pointer1和pointer2交换并将pointer3放入递归
https://leetcode.com/explore/learn/card/recursion-i/250/principle-of-recursion/1681/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swap_pairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pointer1, pointer2, pointer3 = head, head.next, head.next.next
        pointer2.next = pointer1
        pointer1.next = self.swap_pairs(pointer3)
        return pointer2


# 测试方法
if __name__ == '__main__':
    headNode = ListNode(1)
    add = headNode
    for i in range(2, 9):
        add.next = ListNode(i)
        add = add.next

    solution = Solution()
    result = solution.swap_pairs(headNode)

