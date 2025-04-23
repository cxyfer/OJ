#
# @lc app=leetcode id=1051 lang=python3
# @lcpr version=30203
#
# [1051] Height Checker
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(x != y for x, y in zip(heights, sorted(heights)))

class Solution2:
    def heightChecker(self, heights: List[int]) -> int:
        cnt = [0] * 101
        for x in heights:
            cnt[x] += 1
        s = 0  # prefix sum
        ans = 0
        for x in range(101):
            for i in range(s, s + cnt[x]):
                ans += heights[i] != x
            s += cnt[x]
        return ans

# Solution = Solution1
Solution = Solution2
# @lc code=end



#
# @lcpr case=start
# [1,1,4,2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [5,1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

#

