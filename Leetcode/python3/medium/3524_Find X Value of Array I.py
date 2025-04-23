#
# @lc app=leetcode id=3524 lang=python3
#
# [3524] Find X Value of Array I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
DP (刷表法)

注意到 k 的範圍很小，因此可以令 f[i][j] 表示以 nums[i] 結尾的非空子陣列中，有多少個子陣列的乘積 mod k = j 。

但從 f[i] 很難推出轉移來源，這時可以從 f[i-1][j] 下手
f[i-1][j] 可以更新 f[i][(j * nums[i]) % k]
"""
# @lc code=start
class Solution1:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        f = [[0] * k for _ in range(n + 1)]
        for i, v in enumerate(nums, 1):
            v = v % k
            for j in range(k):
                f[i][(j * v) % k] += f[i - 1][j]
            f[i][v] += 1
        return [sum(f[i][j] for i in range(n+1)) for j in range(k)]
    
class Solution2:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        f = [0] * k
        ans = [0] * k
        for i, v in enumerate(nums):
            nf = [0] * k
            v = v % k
            for j in range(k):
                nf[(j * v) % k] += f[j]
            nf[v] += 1
            ans = [ans[j] + nf[j] for j in range(k)]
            f = nf
        return ans
    
# Solution = Solution1
Solution = Solution2
# @lc code=end

