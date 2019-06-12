"""
设计一个链表

https://leetcode.com/explore/learn/card/linked-list/209/singly-linked-list/1290/
"""


class MyLinkedList(object):
    def __init__(self):
        self.val = []

    def get(self, index: int) -> int:
        if index < 0 or index >= len(self.val): return -1
        return self.val[index]

    def addAtHead(self, val: int) -> None:
        self.val = [val] + self.val

    def addAtTail(self, val: int) -> None:
        self.val.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < -1 or index > len(self.val): return
        li = self.val
        self.val = li[:index] + [val] + li[index:]

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= len(self.val): return
        del self.val[index]
