#
# @lc app=leetcode id=1213 lang=python3
# @lcpr version=30204
#
# [1213] Intersection of Three Sorted Arrays
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        n1, n2, n3 = len(arr1), len(arr2), len(arr3)
        i = j = k = 0
        ans = []
        while i < n1 and j < n2 and k < n3:
            if arr1[i] == arr2[j] == arr3[k]:
                ans.append(arr1[i])
                i += 1
                j += 1
                k += 1
            elif arr1[i] < arr2[j]:
                i += 1
            elif arr2[j] < arr3[k]:
                j += 1
            else:
                k += 1
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n[1,2,5,7,9]\n[1,3,4,5,8]\n
# @lcpr case=end

# @lcpr case=start
# [197,418,523,876,1356]\n[501,880,1593,1710,1870]\n[521,682,1337,1395,1764]\n
# @lcpr case=end

#

