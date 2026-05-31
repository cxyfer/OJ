#
# @lc app=leetcode id=719 lang=python3
# @lcpr version=30204
#
# [719] Find K-th Smallest Pair Distance
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end

"""
令 m 為 pair 的數量，可以視為 m = n^2 / 2
1. 直接排序需要 O(n^2 log n^2)，顯然是不行的
2. 如果 k 的值很小的話可以考慮用 Heap 維護做到 O((n^2) log k)
3. 我原本的想法是基於 Counting Sort，因為 pair distance 的範圍是有限的 (0 ~ 10^6)，所以可以先統計每個 distance 出現的次數，然後從小到大累加次數直到超過 k 就可以了，時間複雜度為 O(n^2 + U)。 (Python TLE, C++ AC)
4. 標準做法是看到 第 k 大/第 k 小的問題，可以思考能不能判斷比 mid 大/小的數量，如果可以的話，就能用 Binary Search 來找到答案。
   而注意到若 nums 為有序的，當固定右端點 r 時，距離 <= mid 的左端點 l 是連續的，且隨著 r 的增加 l 也不會減少，所以可以用雙指針來統計距離 <= mid 的 pair 的數量
   由於只需要一次排序，整體為 O(n log n + n log U)，其中 U 為 distance 的最大值。
"""
# @lc code=start


# Python TLE, C++ AC
# 1e8 + 1e6 對 Python 來說是太勉強了
class Solution1:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)
        U = max(nums) - min(nums)
        cnt = [0] * (U + 1)

        for i, x in enumerate(nums):
            for j in range(i + 1, n):
                y = nums[j]
                cnt[abs(y - x)] += 1

        for x, v in enumerate(cnt):
            if k <= v:
                return x
            k -= v
        return -1


class Solution2:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        def check(mid: int) -> bool:
            cnt = l = 0
            for r, y in enumerate(nums):
                l = bisect_left(nums, y - mid, 0, r)
                cnt += r - l
            return cnt >= k

        left, right = 0, nums[-1] - nums[0]
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left


class Solution3:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        def check(mid: int) -> bool:
            cnt = 0
            l = 0
            for r, y in enumerate(nums):
                while y - nums[l] > mid:
                    l += 1
                cnt += r - l  # [l, r - 1]
            return cnt >= k

        left, right = 0, nums[-1] - nums[0]
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left


# Solution = Solution1  # Python TLE, C++ AC
# Solution = Solution2
Solution = Solution3
# @lc code=end

#
# @lcpr case=start
# [1,3,1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,6,1]\n3\n
# @lcpr case=end

#
