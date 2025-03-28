#
# @lc app=leetcode.cn id=706 lang=python3
#
# [706] 设计哈希映射
#

# @lc code=start
class MyHashMap:
    
    def __init__(self):
        self.buckets = 1009 # 取質數
        self.table = [[] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets
    
    def put(self, key: int, value: int) -> None:
        hashkey = self.hash(key)
        for item in self.table[hashkey]: # 如果已經存在，則更新
            if item[0] == key:
                item[1] = value
                return
        self.table[hashkey].append([key, value]) # 如果不存在，則添加

    def get(self, key: int) -> int:
        hashkey = self.hash(key)
        for item in self.table[hashkey]:
            if item[0] == key: # 如果存在，返回值
                return item[1]
        return -1 # 如果不存在，返回-1

    def remove(self, key: int) -> None:
        hashkey = self.hash(key)
        for idx, item in enumerate(self.table[hashkey]):
            if item[0] == key:
                self.table[hashkey].pop(idx)
                return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end

