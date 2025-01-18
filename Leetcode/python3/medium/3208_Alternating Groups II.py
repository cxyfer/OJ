#
# @lc app=leetcode id=3208 lang=python3
# @lcpr version=30204
#
# [3208] Alternating Groups II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        ans = cnt = 0
        for i in range(n + k - 1):
            if i > 0 and colors[i % n] == colors[(i - 1) % n]:
                cnt = 0
            cnt += 1
            if cnt >= k:
                ans += 1
        return ans
# @lc code=end



#
# @lcpr case=start
# [0,1,0,1,0]\n3\n
# @lcpr case=end

# @lcpr case=start
# [0,1,0,0,1,0,1]\n6\n
# @lcpr case=end

# @lcpr case=start
# [1,1,0,1]\n4\n
# @lcpr case=end

#

