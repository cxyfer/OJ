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
    __slot__ = ["key", "val", "prev", "next"]

    def __init__(self, key=int, val=int):
        self.key = key
        self.val = val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.cache = defaultdict(Node)
        # dummy.next is head, dummy.prev is tail
        self.dummy = Node()
        self.dummy.prev = self.dummy.next = self.dummy

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.moveToHead(node)
        return node.val

    def put(self, key: int, val: int):
        if key in self.cache:
            node = self.cache[key]
            node.val = val
            self.moveToHead(node)
            return
        if self.size == self.capacity:
            self.removeLast()
        node = self.cache[key] = Node(key=key, val=val)
        self.addToHead(node)
        self.size += 1

    def addToHead(self, node: Node) -> None:
        node.prev = self.dummy
        node.next = self.dummy.next
        self.dummy.next.prev = node
        self.dummy.next = node

    def moveToHead(self, node: Node):
        self.remove(node)
        self.addToHead(node)

    def remove(self, node: Node) -> None:  # 刪除節點
        node.prev.next = node.next
        node.next.prev = node.prev

    def removeLast(self) -> None:  # 刪除 list 的最後一個節點
        node = self.dummy.prev
        self.remove(node)
        del self.cache[node.key]
        self.size -= 1
# @lc code=end

obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))
obj.put(3, 3)
print(obj.get(2))
obj.put(4, 4)
