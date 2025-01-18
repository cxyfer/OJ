#
# @lc app=leetcode id=1535 lang=python3
# @lcpr version=30202
#
# [1535] Find the Winner of an Array Game
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k >= n - 1: # if k >= n - 1, only max value can win k times
            return max(arr)
        cur = arr[0] # current max candidate
        win = 0 # current win count
        for i in range(1, n):
            if arr[i] > cur: # new candidate
                cur = arr[i]
                win = 0
            win += 1
            if win == k:
                break
        return cur
# @lc code=end



#
# @lcpr case=start
# [2,1,3,5,4,6,7]\n2\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1]\n10\n
# @lcpr case=end

#

