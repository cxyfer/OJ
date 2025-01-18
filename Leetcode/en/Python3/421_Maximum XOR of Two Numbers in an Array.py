# @algorithm @lc id=421 lang=python3 
# @title maximum-xor-of-two-numbers-in-an-array


from en.Python3.mod.preImport import *
# @test([3,10,5,25,2,8])=28
# @test([14,70,53,83,49,91,36,80,92,51,66,70])=127
class Solution:
    """
        1. XOR + Greedy + bit mask
        https://leetcode.cn/problems/maximum-xor-of-two-numbers-in-an-array/solutions/9289/li-yong-yi-huo-yun-suan-de-xing-zhi-tan-xin-suan-f/
    """
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = 0
        mask = 0
        for bit in range(30, -1, -1):
            mask |= (1 << bit)

            seen = set()
            for num in nums:
                seen.add(mask & num)

            # Greedy，逐位確定最大值
            temp = ans | (1 << bit)

            for prefix in seen:
                if temp ^ prefix in seen:
                    ans = temp
                    break
            # if ans:
            #     print(bit, bin(ans)[2:])
        return ans