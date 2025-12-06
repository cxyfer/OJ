#
# @lc app=leetcode id=3766 lang=python3
#
# [3766] Minimum Operations to Make Binary Palindrome
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MAX_X = int(5e3 + 100)

def is_palindrome(x):
    s = bin(x)[2:]
    return s == s[::-1]

arr = []
for x in range(MAX_X):
    if is_palindrome(x):
        arr.append(x)

class Solution:
    def minOperations(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            i = bisect_left(arr, x)
            ans.append(min(arr[i] - x, x - arr[i - 1]))
        return ans
# @lc code=end

