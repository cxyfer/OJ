#
# @lc app=leetcode.cn id=1726 lang=python3
#
# [1726] 同积元组
#
from preImport import *
# @lc code=start
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = Counter()
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                product = nums[i] * nums[j]
                cnt[product] += 1
                if cnt[product] > 1:
                    ans += (cnt[product] - 1) * 8
        return ans
# @lc code=end

