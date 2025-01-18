#
# @lc app=leetcode id=2225 lang=python3
# @lcpr version=30202
#
# [2225] Find Players With Zero or One Losses
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        cnt = defaultdict(int)
        for x, y in matches: # x is winner, y is loser
            cnt[x] = cnt[x] # insert key if not exist
            cnt[y] += 1
        ans = [[], []]
        for p in sorted(cnt.keys()): # 在添加到答案後，在對答案進行排序會略快一些
            if cnt[p] == 0:
                ans[0].append(p)
            elif cnt[p] == 1:
                ans[1].append(p)
        return ans
# @lc code=end



#
# @lcpr case=start
# [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[2,3],[1,3],[5,4],[6,4]]\n
# @lcpr case=end

#

