#
# @lc app=leetcode id=3153 lang=python3
# @lcpr version=30202
#
# [3153] Sum of Digit Differences of All Pairs
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        Counter + 拆位貢獻
        1. 兩次遍歷，賽時寫法
        2. 一次遍歷
    """
    def sumDigitDifferences(self, nums: List[int]) -> int:
        return self.solve1(nums)
        # return self.solve2(nums)
    def solve1(self, nums: List[int]) -> int: # 
        cnt = defaultdict(Counter)
        for x in nums:
            d = 0
            while x:
                cnt[d][x % 10] += 1
                x //= 10
                d += 1
        ans = 0
        for d in cnt:
            tol = sum(cnt[d].values())
            for k, v in cnt[d].items():
                ans += (tol - v) * v
        return ans // 2 # 每對數字會被計算兩次
    def solve2(self, nums: List[int]) -> int:
        ans = 0
        cnt = [[0] * 10 for _ in range(9)] # 每個位數中，每個數字出現的次數。由於 nums[i] < 10^9，即最多9位數
        for i, x in enumerate(nums):
            j = 0
            while x:
                x, d = divmod(x, 10)
                ans += i - cnt[j][d] # 在第i個數字的第j位，前面有 i - cnt[j][d] 個不同的數字，即為對答案的貢獻
                cnt[j][d] += 1
                j += 1
        return ans
# @lc code=end



#
# @lcpr case=start
# [13,23,12]\n
# @lcpr case=end

# @lcpr case=start
# [10,10,10,10]\n
# @lcpr case=end

#

