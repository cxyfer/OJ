# @algorithm @lc id=2413 lang=python3 
from en.Python3.mod.preImport import *
# @title smallest-number-in-infinite-set
class SmallestInfiniteSet:

    def __init__(self):
        self.visited = set() # 紀錄該元素是否在 SmallestInfiniteSet 中
        self.hp = [] # MinHeap，保存addBack()添加的元素
        self.idx = 1 # 最小的元素位置

    def popSmallest(self) -> int:
        if self.hp:
            val = heappop(self.hp)
            self.visited.remove(val)
        else:
            val = self.idx
            self.idx += 1
        return val

    def addBack(self, num: int) -> None:
        if num >= self.idx or num in self.visited: # 已經在 SmallestInfiniteSet 中
            return
        heappush(self.hp, num)
        self.visited.add(num)
            