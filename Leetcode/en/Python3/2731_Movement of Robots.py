# @algorithm @lc id=2787 lang=python3 
# @title movement-of-robots


from en.Python3.mod.preImport import *
# @test([-2,0,2],"RLL",3)=8
# @test([1,0],"RL",2)=5
class Solution:
    """
        兩個機器人相撞可以視為兩個機器人交換，因為所求的是距離和，所以可以把所有機器人視為相同的
        計算兩兩之間的距離時，使用前綴和
    """
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        MOD = 10**9 + 7
        for idx, dir in enumerate(s):
            nums[idx] += d if dir == 'R' else -d
        nums.sort()
        # 計算兩兩之間的距離
        ans = 0
        pre = 0 # prefix sum
        for idx, num in enumerate(nums):
            ans += idx * num - pre
            pre += num
        return ans % MOD