#
# @lc app=leetcode id=1865 lang=python3
#
# [1865] Finding Pairs With a Certain Sum
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.cnt1 = Counter(nums1)
        self.cnt2 = Counter(nums2)
        self.nums2 = nums2

    def add(self, index: int, val: int) -> None:
        self.cnt2[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.cnt2[self.nums2[index]] += 1
       
    def count(self, tot: int) -> int:
        ans = 0
        for k, v in self.cnt1.items():
            ans += v * self.cnt2[tot - k]
        return ans

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
# @lc code=end

