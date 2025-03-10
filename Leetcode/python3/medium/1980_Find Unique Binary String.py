#
# @lc app=leetcode id=1980 lang=python3
# @lcpr version=30204
#
# [1980] Find Unique Binary String
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1. Hash Set
2. Cantor's Diagonal Argument
"""
# @lc code=start
class Solution1:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        upper = 1 << n - 1
        st = set([int(num, 2) for num in nums])
        for x in range(upper + 1):
            if x in st:
                continue
            return bin(x)[2:].zfill(n)

class Solution2:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        ans = ""
        for i in range(n):
            ans += "1" if nums[i][i] == "0" else "0"
        return ans
    
class Solution(Solution2):
    pass
# @lc code=end

sol = Solution()
print(sol.findDifferentBinaryString(["01","10"])) # "11"
print(sol.findDifferentBinaryString(["00","01"])) # "11"
print(sol.findDifferentBinaryString(["111","011","001"])) # "101"

#
# @lcpr case=start
# ["01","10"]\n
# @lcpr case=end

# @lcpr case=start
# ["00","01"]\n
# @lcpr case=end

# @lcpr case=start
# ["111","011","001"]\n
# @lcpr case=end

#

