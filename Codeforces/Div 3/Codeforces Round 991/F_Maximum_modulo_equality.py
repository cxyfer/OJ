"""
    同餘定理 + 線段樹

    若兩個數A、B ，滿足 A % M == B % M，則兩個數的差值 (A - B) % M == 0，即 M 是 (A - B) 的因數。
    故求最大的 M 等同求兩數之差的最大公因數，可以計算 diffs 陣列，其中 diffs[i] = abs(A[i+1] - A[i])。

    而求區間 [l, r] 的最大 M 值，等同求 diffs[l] ~ diffs[r-1] 的最大公因數，這可以用線段樹維護。
"""
from math import gcd

class SegmentTree:
    def __init__(self, nums):
        n = len(nums)
        self.nums = [0] + nums # 讓 index 從 1 開始
        # self.tree = [0 for _ in range(4 * n)]
        self.tree = [0 for _ in range(1 << (n.bit_length() + 1))]
        self.build(1, 1, n)
 
    def build(self, o, left, right): # node, left, right
        if left == right: # Leaf node initialization
            self.tree[o] = self.nums[left]
            return
        mid = (left + right) // 2
        self.build(o << 1, left, mid) # left child
        self.build(o << 1 | 1, mid + 1, right) # right child
        self.tree[o] = self.merge(o << 1, o << 1 | 1)
 
    def merge(self, left_child, right_child):
        return gcd(self.tree[left_child], self.tree[right_child])
 
    def query(self, o, left, right, l, r):
        if l <= left and right <= r:
            return self.tree[o]
        mid = (left + right) // 2
        ans = 0
        if l <= mid:
            ans = gcd(ans, self.query(o << 1, left, mid, l, r))
        if r > mid:
            ans = gcd(ans, self.query(o << 1 | 1, mid + 1, right, l, r))
        return ans

t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    A = list(map(int, input().split()))
    diffs = [abs(A[i+1] - A[i]) for i in range(n-1)]
    st = SegmentTree(diffs) if n > 1 else None
    ans = []
    for __ in range(q):
        l, r = map(int, input().split())
        if l == r or not diffs:
            ans.append('0')
        else:
            ans.append(st.query(1, 1, n-1, l, r-1))
    print(*ans)