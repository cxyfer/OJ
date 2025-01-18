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
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # return self.solve1(heights)
        return self.solve2(heights)
    def solve1(self, heights: List[int]) -> int:
        expected = sorted(heights)
        ans = 0
        for x, y in zip(heights, expected):
            ans += (x != y)
        return ans
    def solve2(self, heights: List[int]) -> int:
        cnt = [0] * 101
        for x in heights:
            cnt[x] += 1
        s = 0 # prefix sum
        ans = 0
        for i in range(101):
            for j in range(s, s + cnt[i]):
                if heights[j] != i:
                    ans += 1
            s += cnt[i]
        return ans
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

