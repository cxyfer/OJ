# @algorithm @lc id=2107 lang=python3 
# @title find-unique-binary-string


from en.Python3.mod.preImport import *
# @test(["01","10"])="11"
# @test(["00","01"])="11"
# @test(["111","011","001"])="101"
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
    def solveByDiagonal(self, nums: List[str]) -> str:
        n = len(nums)
        ans = ""
        for i in range(n):
            ans += "1" if nums[i][i] == "0" else "0"
        return ans