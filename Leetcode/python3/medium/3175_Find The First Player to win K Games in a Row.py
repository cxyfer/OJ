#
# @lc app=leetcode id=3175 lang=python3
# @lcpr version=30203
#
# [3175] Find The First Player to win K Games in a Row
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        Same as 1535. Find the Winner of an Array Game
    """
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        k = min(k, n)
        ans = 0  # index of the player wins k games
        cnt = 0
        for i in range(1, n):
            if skills[i] > skills[ans]:
                ans = i
                cnt = 0
            cnt += 1
            if cnt == k:
                break
        return ans
# @lc code=end



#
# @lcpr case=start
# [4,2,6,3,9]\n2\n
# @lcpr case=end

# @lcpr case=start
# [2,5,4]\n3\n
# @lcpr case=end

#
