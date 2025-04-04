# @algorithm @lc id=3197 lang=python3 
# @title maximum-strong-pair-xor-ii


from en.Python3.mod.preImport import *
# @test([1,2,3,4,5])=7
# @test([10,100])=0
# @test([500,520,2500,3000])=1020
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