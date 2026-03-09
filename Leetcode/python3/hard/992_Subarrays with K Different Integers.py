#
# @lc app=leetcode id=992 lang=python3
#
# [992] Subarrays with K Different Integers
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # 至少有 lim 個不同的數字的子陣列有多少個
        def calc(lim: int) -> int:
            res = left = 0
            cnt = defaultdict(int)
            for right, x in enumerate(nums):
                cnt[x] += 1
                while len(cnt) >= lim:
                    y = nums[left]
                    cnt[y] -= 1
                    if cnt[y] == 0:
                        del cnt[y]
                    left += 1
                res += left
            return res
        # 恰好 k 個 = 至少 k 個 - 至少 k + 1 個
        return calc(k) - calc(k + 1)
# @lc code=end

