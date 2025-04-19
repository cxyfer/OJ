#
# @lc app=leetcode id=2563 lang=python3
# @lcpr version=30204
#
# [2563] Count the Number of Fair Pairs
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1. Sorting + Binary Search
由於順序不影響 Fair Pairs 的對數，只需要確保不重複計算即可，因此可以先對nums進行排序。

然後對於每個 i，找到有多少 j 可以使 lower <= nums[i] + nums[j] <= upper
即 lower - nums[i] <= nums[j] <= upper - nums[i]，這可以透過二分搜尋來找到。

但注意不能包含 (i, i) 這種情況，以及不能重複計算。
這可以透過限制二分的範圍在 [0, i) 或 [i + 1, n) 來解決：
或是也能先不管，但先扣掉 (i, i) 的情況後，最後再除以 2 即可。

2. Sorting + Two Pointers
使用前綴和或數學排容的思想，求 lo <= x + y <= hi 的對數，等同求 x + y <= hi 的對數減去 x + y < lo 的對數。
而如果我們能確保 x 從小枚舉到大，那麼滿足條件的 y 只會越來越小，
如此一來我們就可以使用 Two Pointers 來找到滿足條件的 y 了。
"""
# @lc code=start
class Solution1:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        ans = 0
        nums.sort()
        for i, x in enumerate(nums):
            l = bisect_left(nums, lower - x, 0, i) # [0, idx)
            r = bisect_right(nums, upper - x, 0, i) - 1 # [0, idx)
            ans += r - l + 1
        return ans
    
class Solution2:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        nums.sort()
        # 計算有多少個 pair 滿足 nums[i] + nums[j] <= hi
        def f(hi: int) -> int:
            res = 0
            j = n - 1
            for i, x in enumerate(nums):
                while j > i and x + nums[j] > hi:  # 太大了，需要縮小右端點
                    j -= 1
                if j == i:
                    break
                res += j - i
            return res
        return f(upper) - f(lower - 1)

# Solution = Solution1
Solution = Solution2
# @lc code=end



#
# @lcpr case=start
# [0,1,7,4,4,5]\n3\n6\n
# @lcpr case=end

# @lcpr case=start
# [1,7,9,2,5]\n11\n11\n
# @lcpr case=end

#

