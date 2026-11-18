#
# @lc app=leetcode id=53 lang=python3
# @lcpr version=30204
#
# [53] Maximum Subarray
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
見筆記: https://gdst.dev/posts/LC-53/

1. 前綴和 + 枚舉右維護左
首先做前綴和 s ，如此便可以把區間和轉換為兩個前綴和的差。
之後，對於每個固定的右端點 right ，為使 s[right] - s[left] 最大，只需要維護最小的 s[left] 即可

2. 動態規劃
定義 f[i] = max(f[i-1] + nums[i], nums[i])，即以 nums[i] 為右端點的最大子陣列和

3. 分治
"""
# @lc code=start
class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float("-inf")
        s = mn = 0
        for x in nums:
            s += x
            ans = max(ans, s - mn)
            mn = min(mn, s)
        return ans


class Solution2a:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        f = [-float("inf")] * (n + 1)
        for i, x in enumerate(nums):
            f[i + 1] = max(f[i] + x, x)
        return max(f)


class Solution2b:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -float("inf")
        f = 0
        for x in nums:
            f = max(f + x, x)
            ans = max(ans, f)
        return ans


class Node:
    def __init__(self, lSum, rSum, mSum, tot):
        self.lSum = lSum
        self.rSum = rSum
        self.mSum = mSum
        self.tot = tot


class Solution3:
    def maxSubArray(self, nums: List[int]) -> int:
        def query(l, r):
            if l == r:
                return Node(nums[l], nums[l], nums[l], nums[l])
            mid = (l + r) >> 1
            ls = query(l, mid)
            rs = query(mid + 1, r)
            # Combine
            lSum = max(ls.lSum, ls.tot + rs.lSum)
            rSum = max(rs.rSum, rs.tot + ls.rSum)
            mSum = max(ls.mSum, rs.mSum, ls.rSum + rs.lSum)
            tot = ls.tot + rs.tot
            return Node(lSum, rSum, mSum, tot)

        return query(0, len(nums) - 1).mSum


# Solution = Solution1
# Solution = Solution2a
# Solution = Solution2b
Solution = Solution3
# @lc code=end


#
# @lcpr case=start
# [-2,1,-3,4,-1,2,1,-5,4]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [5,4,-1,7,8]\n
# @lcpr case=end

#
