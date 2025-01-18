#
# @lc app=leetcode id=1310 lang=python3
# @lcpr version=30204
#
# [1310] XOR Queries of a Subarray
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        XOR Prefix Sum
    """
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        s = [0] * (n + 1) # s[i] = arr[0] ^ arr[1] ^ ... ^ arr[i-1]
        for i, x in enumerate(arr):
            s[i + 1] = s[i] ^ x
        return [s[r + 1] ^ s[l] for l, r in queries]
# @lc code=end



#
# @lcpr case=start
# [1,3,4,8]\n[[0,1],[1,2],[0,3],[3,3]]\n
# @lcpr case=end

# @lcpr case=start
# [4,8,2,10]\n[[2,3],[1,3],[0,0],[0,3]]\n
# @lcpr case=end

#

