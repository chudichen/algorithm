"""
判断是否为循环链表

采用快慢指针
https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1212/
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next or not head.next.next:
            return False
        fast, slow = head.next.next, head
        while fast and fast.next and slow:
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next.next
        return False

