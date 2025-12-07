"""
CSES-1077 Sliding Window Cost
https://cses.fi/problemset/task/1077

在 CSES-1076 Sliding Window Median 的基礎上，額外維護堆中元素的總和
注意 pushpop 操作不會雖然不會影響 sz ，但會影響 sum
"""
from collections import defaultdict
from heapq import heappush, heappop, heappushpop

# 模板來源 https://leetcode.cn/circle/discuss/mOr1u6/
class LazyHeap:
    def __init__(self):
        self.hp = []
        self.cnt = defaultdict(int)  # 需要刪除的次數
        self.sz = 0  # 實際大小
        self.sum = 0

    def remove(self, x: int) -> None:
        self.cnt[x] += 1  # 懶刪除
        self.sz -= 1
        self.sum -= x

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
        x = heappop(self.hp)
        self.sum -= x
        return x

    def push(self, x: int) -> None:
        heappush(self.hp, x)
        self.sz += 1
        self.sum += x

    def pushpop(self, x: int) -> int:
        self.apply_remove()
        self.sum += x
        y = heappushpop(self.hp, x)
        self.sum -= y
        return y

def solve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    assert len(A) == n
    
    ans = []
    L, R = LazyHeap(), LazyHeap()
    for r, x in enumerate(A):
        # 1. 入窗口，保證 L.sz == R.sz 或 L.sz == R.sz + 1
        if L.sz == R.sz:
            L.push(-R.pushpop(x))
        else:
            R.push(-L.pushpop(-x))

        if r >= k - 1:
            # 2. 更新答案，最小代價為 sum(abs(x - median))
            median = -L.top()
            ans.append((median * L.sz + L.sum) + (R.sum - median * R.sz))
            # 3. 出窗口
            y = A[r - k + 1]
            if y <= -L.top():  # 刪除的元素在左堆
                L.remove(-y)
                if L.sz < R.sz:  # 平衡大小
                    L.push(-R.pop())
            else:  # 刪除的元素在右堆
                R.remove(y)
                if L.sz > R.sz + 1:  # 平衡大小
                    R.push(-L.pop())
    print(*ans)

if __name__ == "__main__":
    solve()