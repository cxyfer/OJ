#
# @lc app=leetcode id=845 lang=python3
#
# [845] Longest Mountain in Array
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0
        ans = 0
        i = 0
        while i < n - 2:
            st = i
            while i < n - 1 and arr[i] < arr[i + 1]:
                i += 1
            if i == st:
                i += 1
                continue
            md = i
            while i < n - 1 and arr[i] > arr[i + 1]:
                i += 1
            if i == md:
                i += 1
                continue
            ans = max(ans, i - st + 1)
        return ans
# @lc code=end

