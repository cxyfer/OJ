#
# @lc app=leetcode.cn id=2935 lang=python3
#
# [2935] 找出强数对的最大异或值 II
#
from typing import List
# @lc code=start
class Solution:
    """
        Similar to 421. Maximum XOR of Two Numbers in an Array
        假設 x < y，則 |x-y| <= min(x, y) => 2x >= y
    """
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort() # 確保x < y
        ans = 0
        mask = 0
        for bit in range(30, -1, -1):
            mask |= (1 << bit)

            # Greedy，逐位確定最大值
            new_ans = ans | (1 << bit) # 這個位元是否可以為 1

            dic = dict()
            for y in nums:
                mask_y = y & mask
                target = new_ans ^ mask_y
                if target in dic and dic[target] * 2 >= y: # 2x >= y
                    ans = new_ans # 這個位元可以為 1
                    break
                dic[mask_y] = y
        return ans
# @lc code=end

