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
        st = set([int(x, 2) for x in nums])
        for x in range(1 << n):
            if x in st:
                continue
            return f"{x:b}".zfill(n)
        return ""


class Solution2:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # return ''.join('1' if num[i] == '0' else '0' for i, num in enumerate(nums))
        n = len(nums)
        ans = [''] * n
        for i, num in enumerate(nums):
            ans[i] = '1' if num[i] == '0' else '0'
        return "".join(ans)


# Solution = Solution1
Solution = Solution2
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

