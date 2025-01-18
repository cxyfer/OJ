#
# @lc app=leetcode id=2748 lang=python3
# @lcpr version=30204
#
# [2748] Number of Beautiful Pairs
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                y = nums[i]
                while y >= 10:
                    y //= 10
                x = nums[j] % 10
                if gcd(y, x) == 1:
                    ans += 1
        return ans
    
class Solution2:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        ans = 0
        cnt = [0] * 10
        for x in nums:
            for y in range(1, 10):
                if gcd(y, x % 10) == 1:
                    ans += cnt[y]
            while x >= 10:
                x //= 10
            cnt[x] += 1
        return ans

class Solution(Solution1):
# class Solution(Solution2):
    pass
# @lc code=end



#
# @lcpr case=start
# [2,5,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [11,21,12]\n
# @lcpr case=end

#

