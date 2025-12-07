from collections import defaultdict
from heapq import heappush, heappop, heappushpop

# 模板來源 https://leetcode.cn/circle/discuss/mOr1u6/
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
            # 2. 更新答案，若 k 為偶數可能有不同定義，但這裡兩者都相同
            ans.append(-L.top())
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