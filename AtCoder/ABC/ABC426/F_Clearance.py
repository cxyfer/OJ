"""
Divide and Conquer + Lazy Segment Tree

根據題意，我們需要關注區間內非零元素的值：
- 如果區間內所有非零元素的值都 > k，那麼可以直接做區間更新，並回傳區間內非零元素的個數 node.cnt * k
- 如果區間內存在非零元素的值 <= k，那麼需要遞迴到子區間，並回傳子區間的答案，並向上更新。
  - 當 node.mn = k 時，看似可以直接做區間更新，但其實會影響到 node.cnt 的值，這時也需要遞迴到子區間
"""

from typing import List

class SegmentTree:
    def __init__(self, v: List[int] = None):
        if isinstance(v, int):
            self.n = v
        elif isinstance(v, list):
            self.n = len(v)
        sz = 1 << (self.n.bit_length() + 1)
        self.mn = [float('inf')] * sz
        self.cnt = [0] * sz
        self.lazy = [0] * sz
        if isinstance(v, list):
            self.build(1, 1, self.n, v)

    def build(self, o: int, left: int, right: int, nums: List[int]) -> None:
        if left == right:
            self.mn[o] = nums[left - 1]
            self.cnt[o] = 1 if nums[left - 1] != 0 else 0
            return
        mid = (left + right) // 2
        self.build(o << 1, left, mid, nums)
        self.build(o << 1 | 1, mid + 1, right, nums)
        self.pushup(o)  # push up node value

    # push up node value
    def pushup(self, o: int) -> None:
        # Update method (Customized)
        self.mn[o] = min(self.mn[o << 1], self.mn[o << 1 | 1])
        self.cnt[o] = self.cnt[o << 1] + self.cnt[o << 1 | 1]

    # push down lazy tags
    def pushdown(self, o: int, left: int, right: int) -> None:
        if self.lazy[o] != 0:
            # Update node value (Customized)
            mid = (left + right) // 2
            self._update(o << 1, left, mid, self.lazy[o])
            self._update(o << 1 | 1, mid + 1, right, self.lazy[o])
            self.lazy[o] = 0
    
    # update node value (Customized)
    def _update(self, o: int, left: int, right: int, v: int) -> None:
        if self.cnt[o] == 0:
            return
        self.mn[o] += v
        self.lazy[o] += v

    # query the range [l, r] with value k
    def _query(self, o: int, left: int, right: int, l: int, r: int, k: int) -> None:
        if self.cnt[o] == 0:
            return 0
        if l <= left and right <= r and self.mn[o] > k:
            self._update(o, left, right, -k)
            return k * self.cnt[o]
        if left == right:
            ans = self.mn[o]
            self.cnt[o] = self.lazy[o] = 0
            self.mn[o] = float('inf')
            return ans
        # Ensure all lazy tags have been pushed down
        self.pushdown(o, left, right) 
        mid = (left + right) // 2
        # Calculate answer (Customized)
        ans = 0
        if l <= mid:
            ans += self._query(o << 1, left, mid, l, r, k)
        if r > mid:
            ans += self._query(o << 1 | 1, mid + 1, right, l, r, k)
        self.pushup(o)
        return ans

    def query(self, l: int, r: int, k: int) -> int:
        return self._query(1, 1, self.n, l, r, k)

def solve():
    N = int(input())
    A = list(map(int, input().split()))

    assert len(A) == N
    seg = SegmentTree(A)

    Q = int(input())
    for _ in range(Q):
        l, r, k = map(int, input().split())
        print(seg.query(l, r, k))

if __name__ == "__main__":
    solve()