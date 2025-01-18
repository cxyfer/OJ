#
# @lc app=leetcode.cn id=421 lang=python3
#
# [421] 数组中两个数的最大异或值
#
from typing import *
# @lc code=start
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
# @lc code=end
sol = Solution()
print(sol.findMaximumXOR([3,10,5,25,2,8])) # 28
print(sol.findMaximumXOR([14,70,53,83,49,91,36,80,92,51,66,70])) # 127