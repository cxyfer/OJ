#
# @lc app=leetcode id=3447 lang=python3
# @lcpr version=30204
#
# [3447] Assign Elements to Groups with Constraints
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        mx = max(groups)
        mp = [-1] * (mx + 1)
        for i, x in enumerate(elements):
            if x > mx or mp[x] != -1:
                continue
            for y in range(x, mx + 1, x):
                if mp[y] == -1:
                    mp[y] = i
        return [mp[x] for x in groups]
# @lc code=end


#
# @lcpr case=start
# [8,4,3,2,4]\n[4,2]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,5,7]\n[5,3,3]\n
# @lcpr case=end

# @lcpr case=start
# [10,21,30,41]\n[2,1]\n
# @lcpr case=end

#

