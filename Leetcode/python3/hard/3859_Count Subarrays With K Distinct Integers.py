#
# @lc app=leetcode id=3859 lang=python3
#
# [3859] Count Subarrays With K Distinct Integers
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countSubarrays(self, nums: list[int], k: int, m: int) -> int:
        # 當有至少 lim 個不同的數字、且有 k 個數字出現至少 m 次時，有多少個子陣列符合條件
        def calc(lim: int) -> int:
            res = left = ge_m = 0
            cnt = defaultdict(int)
            for right, x in enumerate(nums):
                cnt[x] += 1
                if cnt[x] == m:
                    ge_m += 1
                while len(cnt) >= lim and ge_m >= k:
                    y = nums[left]
                    if cnt[y] == m:
                        ge_m -= 1
                    cnt[y] -= 1
                    if cnt[y] == 0:
                        del cnt[y]
                    left += 1
                res += left
            return res
        # 恰好 k 個 = 至少 k 個 - 至少 k + 1 個
        return calc(k) - calc(k + 1)
# @lc code=end

