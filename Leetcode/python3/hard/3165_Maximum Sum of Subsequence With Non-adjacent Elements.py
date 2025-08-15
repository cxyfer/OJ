#
# @lc app=leetcode id=3165 lang=python3
# @lcpr version=30202
#
# [3165] Maximum Sum of Subsequence With Non-adjacent Elements
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MOD = int(1e9) + 7
class SegNode:
    def __init__(self):
        self.f = [0, 0, 0, 0]

    def __add__(self, other):
        # f00: 不選 left, 不選 right
        # f01: 不選 left, 可選可不選 right
        # f10: 可選可不選 left, 不選 right
        # f11: 可選可不選 left, 可選可不選 right
        res = SegNode()
        res.f[0] = max(self.f[0] + other.f[2], self.f[1] + other.f[0])
        res.f[1] = max(self.f[0] + other.f[3], self.f[1] + other.f[1])
        res.f[2] = max(self.f[2] + other.f[2], self.f[3] + other.f[0])
        res.f[3] = max(self.f[2] + other.f[3], self.f[3] + other.f[1])
        return res

class SegmentTree:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums
        self.tree = [SegNode() for _ in range(4 * self.n)]
        self.build(1, 1, self.n)

    def build(self, o, left, right) -> None:  # node, left, right
        if left == right:  # Leaf node initialization
            self.tree[o].f[3] = max(self.nums[left - 1], 0)  # f11 
            return
        mid = (left + right) // 2
        self.build(o << 1, left, mid)
        self.build(o << 1 | 1, mid + 1, right)
        self.pushup(o)

    def pushup(self, o) -> None:
        # tree[o] = tree[o << 1] + tree[o << 1 | 1]  # 這樣寫需要重新建構 SegNode，會 TLE
        l00, l01, l10, l11 = self.tree[o << 1].f
        r00, r01, r10, r11 = self.tree[o << 1 | 1].f
        self.tree[o].f[0] = max(l00 + r10, l01 + r00)  # f00 表示不選 left, 不選 right
        self.tree[o].f[1] = max(l00 + r11, l01 + r01)  # f01 表示不選 left, 可選可不選 right
        self.tree[o].f[2] = max(l10 + r10, l11 + r00)  # f10 表示可選可不選 left, 不選 right
        self.tree[o].f[3] = max(l10 + r11, l11 + r01)  # f11 表示可選可不選 left, 可選可不選 right

    def _update(self, o, left, right, idx, val) -> None:
        if left == right:
            self.tree[o].f[3] = max(val, 0)
            return
        mid = (left + right) // 2
        if idx <= mid:
            self._update(o << 1, left, mid, idx, val)
        else:
            self._update(o << 1 | 1, mid + 1, right, idx, val)
        self.pushup(o)

    def _query(self, o, left, right, l, r) -> SegNode:
        if left == l and r == right:
            return self.tree[o]
        mid = (left + right) // 2
        if r <= mid:
            return self._query(o << 1, left, mid, l, r)
        if mid < l:
            return self._query(o << 1 | 1, mid + 1, right, l, r)
        return self._query(o << 1, left, mid, l, mid) + self._query(o << 1 | 1, mid + 1, right, mid + 1, r)

    def update(self, idx, val) -> None:
        self._update(1, 1, self.n, idx, val)

    # def query(self, l, r) -> SegNode:
        # return self._query(1, 1, self.n, l, r)
    @property
    def query(self) -> int:
        return self.tree[1].f[3]

class Solution:
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        seg = SegmentTree(nums)
        ans = 0
        for pos, x in queries:
            seg.update(pos + 1, x)
            ans = (ans + seg.query) % MOD
        return ans
# @lc code=end



#
# @lcpr case=start
# [3,5,9]\n[[1,-2],[0,-3]]\n
# @lcpr case=end

# @lcpr case=start
# [0,-1]\n[[0,-5]]\n
# @lcpr case=end

#

