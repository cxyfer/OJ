from collections import defaultdict
from heapq import heappush, heappop, heappushpop

# 模板来源 https://leetcode.cn/circle/discuss/mOr1u6/
class LazyHeap:
    def __init__(self):
        self.hp = []
        self.cnt = defaultdict(int)  # 需要刪除的次數
        self.sz = 0  # 實際大小

    def remove(self, x: int) -> None:
        self.cnt[x] += 1  # 懶刪除
        self.sz -= 1

    def apply_remove(self) -> None:  # 正式執行刪除操作
        while self.hp and self.cnt[self.hp[0]] > 0:
            self.cnt[self.hp[0]] -= 1
            heappop(self.hp)

    def top(self) -> int:
        self.apply_remove()
        return self.hp[0]

    def pop(self) -> int:
        self.apply_remove()
        self.sz -= 1
        return heappop(self.hp)

    def push(self, x: int) -> None:
        heappush(self.hp, x)
        self.sz += 1

    def pushpop(self, x: int) -> int:
        self.apply_remove()
        return heappushpop(self.hp, x)