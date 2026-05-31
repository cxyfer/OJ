#
# @lc app=leetcode id=2126 lang=python3
#
# [2126] Destroying Asteroids
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end

"""
1. 排序後貪心
2. O(n + log U) 或 O(n) 的做法
利用 2^k + 2^k >= 2^(k + 1) 的性質，將 asteroids 分組
如果當前 mass 可以吃掉某組的最小值，那麼就可以吃掉整組
2b 的寫法可以確保在 n 很小時不會有額外的 log U 的開銷，為 O(n)
"""
# @lc code=start
class Solution1:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        # return (lambda nums: all(s >= x for x, s in zip(nums, accumulate(nums, initial=mass))))(sorted(asteroids))
        asteroids.sort()
        for x in asteroids:
            if mass < x:
                return False
            mass += x
        return True


class Solution2a:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        U = max(asteroids).bit_length()

        sum_ = [0] * (U + 1)
        min_ = [inf] * (U + 1)

        for x in asteroids:
            b = x.bit_length() - 1
            sum_[b] += x
            min_[b] = min(min_[b], x)

        for mn, s in zip(min_, sum_):
            if mn == inf:
                continue
            if mass < mn:
                return False
            mass += s
        return True


class Solution2b:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        sum_ = defaultdict(int)
        min_ = defaultdict(lambda: inf)

        msk = 0  # 出現過的集合
        for x in asteroids:
            b = x.bit_length() - 1
            sum_[b] += x
            min_[b] = min(min_[b], x)
            msk |= 1 << b

        while msk:
            lb = msk & -msk
            b = lb.bit_length() - 1
            if mass < min_[b]:
                return False
            mass += sum_[b]
            msk ^= lb
        return True


# Solution = Solution1
# Solution = Solution2a
Solution = Solution2b
# @lc code=end

