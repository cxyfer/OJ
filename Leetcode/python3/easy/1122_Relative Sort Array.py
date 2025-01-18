#
# @lc app=leetcode id=1122 lang=python3
# @lcpr version=30203
#
# [1122] Relative Sort Array
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        rank = {x: i for i, x in enumerate(arr2)}
        return sorted(arr1, key=lambda x: rank.get(x, 1000 + x))
    
class Solution2:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cnt = [0] * (1001)
        for x in arr1:
            cnt[x] += 1
        
        ans = []
        for x in arr2:
            ans.extend([x] * cnt[x])
            cnt[x] = 0
        for x in range(1001):
            if cnt[x] > 0:
                ans.extend([x] * cnt[x])
        return ans

# class Solution(Solution1):
class Solution(Solution2):
    pass
# @lc code=end


#
# @lcpr case=start
# [2,3,1,3,2,4,6,7,9,2,19]\n[2,1,4,3,9,6]\n
# @lcpr case=end

# @lcpr case=start
# [28,6,22,8,44,17]\n[22,28,8,6]\n
# @lcpr case=end

#

