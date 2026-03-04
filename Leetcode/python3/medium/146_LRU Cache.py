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
class Node:
    __slots__ = ['key', 'value', 'prev', 'next']

    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = dict()
        self.dummy = Node()  # dummy head
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.moveToHead(node)
        return node.value
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                del self.cache[self.removeTail().key]
                self.size -= 1

    def removeNode(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def addToHead(self, node: Node) -> None:
        node.prev = self.dummy
        node.next = self.dummy.next
        node.prev.next = node
        node.next.prev = node

    def moveToHead(self, node: Node) -> None:
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self) -> Node:
        node = self.dummy.prev
        self.removeNode(node)
        return node
# @lc code=end

obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))
obj.put(3, 3)
print(obj.get(2))
obj.put(4, 4)
