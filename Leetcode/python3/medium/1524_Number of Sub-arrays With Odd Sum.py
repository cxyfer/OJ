#
# @lc app=leetcode id=1524 lang=python3
# @lcpr version=30203
#
# [1524] Number of Sub-arrays With Odd Sum
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        s = 0
        ans = 0
        cnt = [1, 0] # cnt[0] = even, cnt[1] = odd
        for x in arr:
            s = (s + x) & 1
            ans += cnt[s ^ 1] # 奇數 - 偶數 = 奇數, 偶數 - 奇數 = 奇數
            ans %= MOD
            cnt[s] += 1
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,3,5]\n
# @lcpr case=end

# @lcpr case=start
# [2,4,6]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,6,7]\n
# @lcpr case=end

#

