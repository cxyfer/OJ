#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
    Double Linked List + Hashmap
"""
# @lc code=start
from collections import defaultdict


class Node:
    __slot__ = ["key", "val", "prev", "next"]

    def __init__(self, key=int, val=int):
        self.key = key
        self.val = val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cnt = 0
        self.capacity = capacity
        self.mp = defaultdict(Node)
        self.head = Node()  # head->next = first
        self.tail = Node()  # tail->prev = last
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.mp:
            return -1
        node = self.mp[key]
        self.moveToFront(node)
        return node.val

    def put(self, key: int, val: int):
        if key in self.mp:
            node = self.mp[key]
            node.val = val
            self.moveToFront(node)
        else:
            node = self.mp[key] = Node(key=key, val=val)
            self.addFront(node)
            self.cnt += 1
            if self.cnt > self.capacity:
                self.removeLast()
                self.cnt -= 1

    def addFront(self, node: Node) -> None:
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def moveToFront(self, node: Node):
        self.remove(node)
        self.addFront(node)

    def remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def removeLast(self):
        node = self.tail.prev
        self.remove(node)
        del self.mp[node.key]
# @lc code=end

obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))
obj.put(3, 3)
print(obj.get(2))
obj.put(4, 4)
