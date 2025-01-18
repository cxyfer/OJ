#
# @lc app=leetcode.cn id=1980 lang=python3
#
# [1980] 找出不同的二进制字符串
#
from preImport import *
# @lc code=start
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # return self.solveByCounter(nums)
        return self.solveByDiagonal(nums)

    def solveByCounter(self, nums: List[str]) -> str:
        n = len(nums)
        upper = 1 << n - 1
        cnt = Counter([int(num, 2) for num in nums])
        for i in range(upper + 1):
            if cnt[i] == 0:
                return bin(i)[2:].zfill(n)
    """
        nums 的長度 n 和 字串的長度也是 n，
        因此可以確保答案和每個數字都有一位不同
    """
    def solveByDiagonal(self, nums: List[str]) -> str:
        n = len(nums)
        ans = ""
        for i in range(n):
            ans += "1" if nums[i][i] == "0" else "0"
        return ans

# @lc code=end
sol = Solution()
print(sol.findDifferentBinaryString(["01","10"])) # "11"
print(sol.findDifferentBinaryString(["00","01"])) # "11"
print(sol.findDifferentBinaryString(["111","011","001"])) # "101"
