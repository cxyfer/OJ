#
# @lc app=leetcode id=3177 lang=python3
# @lcpr version=30203
#
# [3177] Find the Maximum Length of a Good Subsequence II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        if k == 0:
            return max(Counter(nums).values())
        dp = [0 for _ in range(k+1)]
        st = [set() for _ in range(k+1)]
        mx = [defaultdict(int) for _ in range(k+1)]

        for x in nums:
            prev = 0
            for j in range(k+1):
                cur = max(prev + 1, mx[j][x] + 1)
                if x in st[j]:
                    cur = max(cur, (dp[j]+1))
                prev, mx[j][x] = dp[j], cur
                if dp[j] < cur:
                    dp[j] = cur
                    st[j].clear()
                if cur == dp[j]:
                    st[j].add(x)
        return dp[k]
# @lc code=end



#
# @lcpr case=start
# [1,2,1,1,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,1]\n0\n
# @lcpr case=end

#

