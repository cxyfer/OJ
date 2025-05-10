#
# @lc app=leetcode id=2918 lang=python3
#
# [2918] Minimum Equal Sum of Two Arrays After Replacing Zeros
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1a:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        cnt1, cnt2 = nums1.count(0), nums2.count(0)
        s1, s2 = sum(nums1) + cnt1, sum(nums2) + cnt2
        if cnt1 == 0 and cnt2 == 0:
            return s1 if s1 == s2 else -1
        elif cnt1 == 0:
            return s1 if s1 >= s2 else -1
        elif cnt2 == 0:
            return s2 if s2 >= s1 else -1
        else:
            return max(s1, s2)
    
class Solution1b:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        cnt1, cnt2 = nums1.count(0), nums2.count(0)
        s1, s2 = sum(nums1) + cnt1, sum(nums2) + cnt2
        if s1 < s2 and cnt1 == 0 or s2 < s1 and cnt2 == 0:
            return -1
        return max(s1, s2)

# Solution = Solution1a
Solution = Solution1b
# @lc code=end
