"""
删除链表中的元素

借助一个前指针，如果有值等于目标值，则将前指针指向下一个元素
https://leetcode.com/problems/remove-linked-list-elements/submissions/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def remove_elements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
        pre = None
        while head and head.val == val:
            head = head.next
        cur = head
        while cur:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return head


if __name__ == '__main__':
    headNode = ListNode(1)
    add = headNode
    for i in range(2, 6):
        add.next = ListNode(i)
        add = add.next
    solution = Solution()
    solution.remove_elements(headNode, 5)
