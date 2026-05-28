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


class Solution3:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        sz = 2 << n.bit_length()
        tree = [0] * sz
        lazy = [0] * sz

        def build(o: int, left: int, right: int) -> None:
            if left == right:
                tree[o] = nums[left]
                return
            mid = (left + right) // 2
            build(o * 2, left, mid)
            build(o * 2 + 1, mid + 1, right)
            pushup(o)

        def pushup(o: int) -> None:
            tree[o] = max(tree[o * 2], tree[o * 2 + 1])

        def _update(o: int, left: int, right: int, v: int) -> None:
            tree[o] += v
            lazy[o] += v

        def pushdown(o: int, left: int, right: int) -> None:
            if lazy[o] == 0 or left == right:
                return
            mid = (left + right) // 2
            _update(o * 2, left, mid, lazy[o])
            _update(o * 2 + 1, mid + 1, right, lazy[o])
            lazy[o] = 0

        def update(o: int, left: int, right: int, l: int, r: int, f: Any) -> None:
            if l <= left and right <= r:
                _update(o, left, right, f)
                return
            pushdown(o, left, right)
            mid = (left + right) // 2
            if l <= mid:
                update(o * 2, left, mid, l, r, f)
            if r > mid:
                update(o * 2 + 1, mid + 1, right, l, r, f)
            pushup(o)

        def apply(l: int, r: int, f: Any) -> None:
            if l > r:
                return
            update(1, 0, n - 1, l, r, f)

        build(1, 0, n - 1)
        if tree[1] <= 0:
            return 0

        for i, (l, r, v) in enumerate(queries, start=1):
            apply(l, r, -v)
            if tree[1] <= 0:
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

