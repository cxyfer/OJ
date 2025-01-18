# @algorithm @lc id=460 lang=python3 
# @title lfu-cache
from collections import defaultdict

class Node:
    __slots__ = 'prev', 'next', 'key', 'value', 'freq' # 靈神說可以節省記憶體，待補
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity # max size
        self.size = 0 # current size
        self.cache = dict() # key: Node

        def new_list(): # 為每個 freq 創建一條Double Linked List
            dummy = Node()
            dummy.prev = dummy
            dummy.next = dummy
            return dummy

        self.freq_map = defaultdict(new_list)
        self.min_freq = 0

    def getNode(self, key: int) -> Node: # 獲取節點並更新 freq
        if key not in self.cache:
            return None
        node = self.cache[key]
        self.remove(node)
        dummy = self.freq_map[node.freq]
        if dummy.next == dummy: # 如果該 freq 的 list 為空，則刪除該 list
            del self.freq_map[node.freq]
            if self.min_freq == node.freq:
                self.min_freq += 1
        node.freq += 1
        self.addToHead(self.freq_map[node.freq], node)
        return node
    
    def get(self, key: int) -> int:
        node = self.getNode(key)
        return node.value if node else -1

    def put(self, key: int, value: int) -> None:
        node = self.getNode(key)
        if node: # 如果 key 存在，則更新 value
            node.value = value
            return
        # 否則創建新節點
        # 如果 cache 已滿，則刪除最不常用的節點
        if self.size == self.capacity:
            # 從最小 freq 的 list 中刪除最後一個節點
            dummy = self.freq_map[self.min_freq] 
            removed = dummy.prev
            del self.cache[removed.key]
            self.size -= 1
            self.remove(removed)
            # 如果該 freq 的 list 為空，則刪除該 list
            if dummy.next == dummy: 
                del self.freq_map[self.min_freq]
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.addToHead(self.freq_map[1], new_node)
        self.min_freq = 1
        self.size += 1

    def remove(self, x: Node) -> None: # 刪除節點
        x.prev.next = x.next
        x.next.prev = x.prev

    def addToHead(self, dummy: Node, x: Node) -> None:
        x.prev = dummy
        x.next = dummy.next
        x.prev.next = x
        x.next.prev = x