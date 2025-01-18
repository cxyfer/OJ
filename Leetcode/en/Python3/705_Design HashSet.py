# @algorithm @lc id=816 lang=python3 
# @title design-hashset
class MyHashSet:

    def __init__(self):
        self.buckets = 1009 # 取質數
        self.table = [[] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets
    
    def add(self, key: int) -> None:
        hashkey = self.hash(key)
        for item in self.table[hashkey]: # 如果已經存在，則跳過
            if item == key:
                return
        self.table[hashkey].append(key)

    def remove(self, key: int) -> None:
        hashkey = self.hash(key)
        for idx, item in enumerate(self.table[hashkey]):
            if item == key:
                self.table[hashkey].pop(idx)
                return

    def contains(self, key: int) -> bool:
        hashkey = self.hash(key)
        for item in self.table[hashkey]: # 如果已經存在，則返回True
            if item == key:
                return True
        return False