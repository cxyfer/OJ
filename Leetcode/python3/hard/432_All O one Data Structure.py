#
# @lc app=leetcode id=432 lang=python3
# @lcpr version=30204
#
# [432] All O`one Data Structure
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
    Double Linked List + Hash Table

    每個節點維護出現次數為 cnt 的 key 集合
"""

class Node:
    __slots__ = ['cnt', 'prev', 'next', 'st']

    def __init__(self, cnt: int = 1, prev: 'Node' = None, next: 'Node' = None):
        self.cnt = cnt
        self.st = set()
        self.prev = prev
        self.next = next

    def __str__(self):
        return f"Node(cnt={self.cnt}, st={self.st}, prev={self.prev.cnt if self.prev else None}, next={self.next.cnt if self.next else None})"
    
    def insert(self, node: 'Node'):
        node.prev = self
        node.next = self.next
        self.next.prev = node
        self.next = node

    def insertLeft(self, node: 'Node'):
        node.prev = self.prev
        node.next = self
        self.prev.next = node
        self.prev = node

    def removeNode(self):
        self.prev.next = self.next
        self.next.prev = self.prev

class AllOne:

    def __init__(self):
        self.head = Node(0) # dummy head
        self.tail = Node(0) # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cnt_to_node = dict()
        self.key_to_node = dict()

    def inc(self, key: str) -> None:
        if key not in self.key_to_node:
            if self.head.next.cnt != 1: # 如果 cnt 不是 1，則需要插入新的 node
                node = Node(1, self.head, self.head.next)
                self.head.next.prev = node
                self.head.next = node
                self.cnt_to_node[1] = node
            else:
                node = self.head.next
            node.st.add(key)
            self.key_to_node[key] = node
        else:
            cur = self.key_to_node[key]
            nxt = cur.next
            if nxt.cnt != cur.cnt + 1: # 如果 next node 的 cnt 不是 cur.cnt + 1，則需要插入新的 node
                nxt = Node(cur.cnt + 1, cur, cur.next)
                cur.next.prev = nxt
                cur.next = nxt
                self.cnt_to_node[cur.cnt + 1] = nxt
            cur.st.remove(key)
            nxt.st.add(key)
            self.key_to_node[key] = nxt
            if len(cur.st) == 0:
                # cur.removeNode()
                cur.next.prev = cur.prev
                cur.prev.next = cur.next
                del self.cnt_to_node[cur.cnt]
            
    def dec(self, key: str) -> None:
        cur = self.key_to_node[key]
        # print("Dec", key, cur)
        pre = cur.prev
        if cur.cnt - 1 == 0:
            cur.st.remove(key)
            del self.key_to_node[key]
        else:
            if cur.cnt - 1 != pre.cnt:
                pre = Node(cur.cnt - 1, cur.prev, cur)
                cur.prev.next = pre
                cur.prev = pre
            else:
                pre = cur.prev
            # print("Insert", key, "to", pre)
            cur.st.remove(key)
            pre.st.add(key)
            self.key_to_node[key] = pre
            self.cnt_to_node[pre.cnt] = pre
        if len(cur.st) == 0:
            # print("Remove", cur)
            # cur.removeNode()
            cur.next.prev = cur.prev
            cur.prev.next = cur.next
            del self.cnt_to_node[cur.cnt]

    def getMaxKey(self) -> str:
        # for c, node in self.cnt_to_node.items():
        #     print(c, node)
        if self.head.next == self.tail:
            return ""
        return next(iter(self.tail.prev.st), "")

    def getMinKey(self) -> str:
        # for c, node in self.cnt_to_node.items():
        #     print(c, node)
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.st), "")

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
# @lc code=end

allOne = AllOne()
allOne.inc("hello")
allOne.inc("hello")
print(allOne.getMaxKey()) # "hello"
print(allOne.getMinKey()) # "hello"
allOne.inc("leet")
print(allOne.getMaxKey()) # "hello"
print(allOne.getMinKey()) # "leet"
print("===========")
allOne = AllOne()
allOne.inc("a")
allOne.inc("b")
allOne.inc("b")
allOne.inc("c")
allOne.inc("c")
allOne.inc("c")
allOne.dec("b")
allOne.dec("b")
print(allOne.getMinKey()) # "a"
allOne.dec("a")
print(allOne.getMaxKey()) # "c"
print(allOne.getMinKey()) # "c"
print("===========")
allOne = AllOne()
allOne.inc("a")
allOne.inc("b")
allOne.inc("b")
allOne.inc("b")
allOne.inc("b")
allOne.dec("b")
allOne.dec("b")
print(allOne.getMaxKey()) # "b"
print(allOne.getMinKey()) # "a"
