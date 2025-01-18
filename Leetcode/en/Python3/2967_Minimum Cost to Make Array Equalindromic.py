# @algorithm @lc id=3229 lang=python3 
# @title minimum-cost-to-make-array-equalindromic


from en.Python3.mod.preImport import *
# @test([1,2,3,4,5])=6
# @test([10,12,13,14,15])=11
# @test([22,33,22,33,22])=22
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        def check(s: str) -> bool: # 檢查 s 是不是回文數
            nn = len(s)
            for i in range(nn):
                if s[i] != s[nn - i - 1]:
                    return False
            return True

        median = nums[n // 2]
        if check(str(median)): # 中位数是回文數
            return sum([abs(x - median) for x in nums])
        l = median - 1
        while (not check(str(l))) and l > 0: # 找到左邊最近的回文數
            l -= 1
        r = median + 1
        while (not check(str(r))) and r < 10 ** 9: # 找到右邊最近的回文數
            r += 1
        cost1 = sum([abs(x - l) for x in nums])
        cost2 = sum([abs(x - r) for x in nums])
        return min(cost1, cost2) # 返回最小的 cost