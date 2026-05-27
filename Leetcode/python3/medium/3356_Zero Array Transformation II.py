#
# @lc app=leetcode.cn id=3356 lang=python3
# @lcpr version=30204
#
# [3356] 零数组变换 II
#


# @lcpr-template-start
from turtle import st

from preImport import *
# @lcpr-template-end
"""
1. Binary Search + Difference Array
Similar:
- P1083 [NOIP 2012 提高组] 借教室
2. Two Pointers + Difference Array
3. Lazy Segment Tree
"""
# @lc code=start
class Solution1:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n, m = len(nums), len(queries)

        def check(k):
            diff = [0] * (n + 1)
            for l, r, v in queries[:k]:
                diff[l] += v
                diff[r + 1] -= v
            return all(s >= x for s, x in zip(accumulate(diff), nums))

        left, right = 0, m
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left if left <= m else -1


class Solution2:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n, m = len(nums), len(queries)
        diff = [0] * (n + 1)
        s = k = 0
        for i, x in enumerate(nums):
            s += diff[i]
            while k < m and s < x:
                l, r, v = queries[k]
                diff[l] += v
                diff[r + 1] -= v
                if l <= i <= r:
                    s += v
                k += 1
            if s < x:
                return -1
        return k


class LazySegmentTree:
    def __init__(
        self,
        v: Optional[Any] = None,
        op: Optional[Callable[[Any, Any], Any]] = None,
        e: Any = 0,
        mapping: Optional[Callable[[Any, Any, int], Any]] = None,
        composition: Optional[Callable[[Any, Any], Any]] = None,
        id_: Any = 0,
    ):
        if v is None:
            self.nums = None
            self.n = 0
        elif isinstance(v, int):
            self.nums = None
            self.n = v
        else:
            self.nums = list(v)
            self.n = len(self.nums)

        self.op = (lambda a, b: a + b) if op is None else op
        self.e = e
        # mapping(f, x, seglen)
        self.mapping = (
            (lambda f, x, seglen: x + f * seglen) if mapping is None else mapping
        )
        self.composition = (lambda f, g: f + g) if composition is None else composition
        self.id = id_

        self.root = 1
        size = 1 << (self.n.bit_length() + 1)
        self.val = [self.e] * size
        self.lazy = [self.id] * size

        if self.nums is not None and self.n > 0:
            self.build(self.root, 1, self.n)

    def build(self, o: int, left: int, right: int) -> None:
        """Build tree from self.nums on interval [left, right]."""
        if left == right:
            self.val[o] = self.nums[left - 1]
            return
        mid = (left + right) // 2
        self.build(o * 2, left, mid)
        self.build(o * 2 + 1, mid + 1, right)
        self.pushup(o)

    def _update(self, o: int, left: int, right: int, f: Any) -> None:
        """Apply lazy tag f to node o covering [left, right]."""
        seglen = right - left + 1
        self.val[o] = self.mapping(f, self.val[o], seglen)
        self.lazy[o] = self.composition(f, self.lazy[o])

    def pushdown(self, o: int, left: int, right: int) -> None:
        """Push lazy tag at node o down to its children."""
        if self.lazy[o] == self.id or left == right:
            return
        mid = (left + right) // 2
        f = self.lazy[o]
        self._update(o * 2, left, mid, f)
        self._update(o * 2 + 1, mid + 1, right, f)
        self.lazy[o] = self.id

    def pushup(self, o: int) -> None:
        """Recompute node value from children."""
        self.val[o] = self.op(self.val[o * 2], self.val[o * 2 + 1])

    def update(self, o: int, left: int, right: int, l: int, r: int, f: Any) -> None:
        """Range apply: apply tag f on interval [l, r]."""
        if l <= left and right <= r:
            self._update(o, left, right, f)
            return
        self.pushdown(o, left, right)
        mid = (left + right) // 2
        if l <= mid:
            self.update(o * 2, left, mid, l, r, f)
        if r > mid:
            self.update(o * 2 + 1, mid + 1, right, l, r, f)
        self.pushup(o)

    # ---------------- external aliases (public API) ----------------
    def apply(self, l: int, r: int, f: Any) -> None:
        """Apply tag f to interval [l, r], 1-indexed."""
        if self.n <= 0 or l > r:
            return
        self.update(self.root, 1, self.n, l, r, f)

    def all_prod(self) -> Any:
        """Return aggregate on [1, n]."""
        if self.n <= 0:
            return self.e
        return self.val[self.root]


class Solution3:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        seg = LazySegmentTree(
            nums, max, 0, lambda f, x, _: x + f, lambda f, g: f + g, 0
        )

        if seg.all_prod() <= 0:
            return 0

        for i, (l, r, v) in enumerate(queries, start=1):
            seg.apply(l + 1, r + 1, -v)
            if seg.all_prod() <= 0:
                return i
        return -1


# Solution = Solution1
# Solution = Solution2
Solution = Solution3
# @lc code=end

sol = Solution()
print(sol.minZeroArray([2,0,2], [[0,2,1],[0,2,1],[1,1,3]]))  # 2
print(sol.minZeroArray([4,3,2,1], [[1,3,2],[0,2,1]]))  # -1
print(sol.minZeroArray([10], [[0,0,5],[0,0,3],[0,0,2],[0,0,1],[0,0,4],[0,0,1],[0,0,4],[0,0,5],[0,0,3],[0,0,4],[0,0,1]]))  # 3

#
# @lcpr case=start
# [2,0,2]\n[[0,2,1],[0,2,1],[1,1,3]]\n
# @lcpr case=end

# @lcpr case=start
# [4,3,2,1]\n[[1,3,2],[0,2,1]]\n
# @lcpr case=end

#

