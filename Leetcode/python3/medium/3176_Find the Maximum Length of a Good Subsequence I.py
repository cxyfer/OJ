#
# @lc app=leetcode id=3176 lang=python3
# @lcpr version=30203
#
# [3176] Find the Maximum Length of a Good Subsequence I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
    令 f[i][j] 以 nums[i] 為結尾，最多出現 j 次相鄰數字不同的最長子序列
    O(n^2 * k)
"""
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)

        @cache
        def dfs(i, k):
            if k < 0:
                return 0
            if i == 0:
                return 1
            res = 0
            for j in range(i - 1, -1, -1):  # 枚舉前一個數字
                if nums[j] != nums[i]:  # 消耗一次 k
                    res = max(res, 1 + dfs(j, k - 1))
                else:
                    res = max(res, 1 + dfs(j, k))
            return res
        
        ans = 0
        for i in range(n):
            ans = max(ans, dfs(i, k))
        return ans
# @lc code=end

sol = Solution()
print(sol.maximumLength([1,2,1,1,3], 2)) # 4
print(sol.maximumLength([1,2,3,4,5,1], 0)) # 2
print(sol.maximumLength([59,60,59,60,60,60], 0)) # 4
print(sol.maximumLength([68,69,68,69,69,68,68], 1)) # 5

#
# @lcpr case=start
# [1,2,1,1,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,1]\n0\n
# @lcpr case=end

#
