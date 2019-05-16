""""
合并两个已经排好序的链表
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and l2:
            return l2
        if not l2 and l1:
            return l1

        res = ListNode(0)
        tem = res
        while l1 or l2:
            if l1.val and l2.val:
                if l1.val < l2.val:
                    tem.next = ListNode(l1.val)
                    tem = tem.next
                    l1 = l1.next
                else:
                    tem.next = ListNode(l2.val)
                    tem = tem.next
                    l2 = l2.next
            if l1 and l2 is None:
                tem.next = l1
                l1 = None
            if l2 and l1 is None:
                tem.next = l2
                l2 = None
        return res.next


if __name__ == '__main__':
    headNode = ListNode(1)
    add = headNode
    for i in range(2, 9):
        add.next = ListNode(i)
        add = add.next
    result = Solution().merge_two_lists(headNode, headNode)
    print(result)
