#
# @lc app=leetcode id=3160 lang=python3
# @lcpr version=30203
#
# [3160] Find the Number of Distinct Colors Among the Balls
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ans = []
        cnt = defaultdict(int) # 每種顏色的球的數量
        color = defaultdict(lambda: -1) # 每個位置的球的顏色
        for x, y in queries:
            if color[x] != -1:
                cnt[color[x]] -= 1
                if cnt[color[x]] == 0:
                    del cnt[color[x]]
            color[x] = y
            cnt[color[x]] += 1
            ans.append(len(cnt))
        return ans
# @lc code=end



#
# @lcpr case=start
# 4\n[[1,4],[2,5],[1,3],[3,4]]\n
# @lcpr case=end

# @lcpr case=start
# 4\n[[0,1],[1,2],[2,2],[3,4],[4,5]]\n
# @lcpr case=end

#

