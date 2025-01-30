#
# @lc app=leetcode id=350 lang=python3
# @lcpr version=30122
#
# [350] Intersection of Two Arrays II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
    1. 基於值域的作法
    2. Hash Table
    3. Two Pointers + Sorting
"""

class Solution1:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # return list((Counter(nums1) & Counter(nums2)).elements())
        cnt1 = [0] * 1001
        cnt2 = [0] * 1001
        for x in nums1:
            cnt1[x] += 1
        for x in nums2:
            cnt2[x] += 1
        ans = []
        for x in range(1001):
            ans += [x] * min(cnt1[x], cnt2[x])
        return ans
    
class Solution2:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt = [0] * 1001
        for x in nums1:
            cnt[x] += 1
        ans = []
        for x in nums2:
            if cnt[x] > 0:
                ans.append(x)
                cnt[x] -= 1
        return ans
    
class Solution3:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
    
        m, n = len(nums1), len(nums2)
        i, j = 0, 0
        ans = []
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                ans.append(nums1[i])
                i += 1
                j += 1
        return ans
    
# class Solution(Solution1):
class Solution(Solution2):
# class Solution(Solution3):
    pass
# @lc code=end



#
# @lcpr case=start
# [1,2,2,1]\n[2,2]\n
# @lcpr case=end

# @lcpr case=start
# [4,9,5]\n[9,4,9,8,4]\n
# @lcpr case=end

#
