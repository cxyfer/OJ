# @algorithm @lc id=45 lang=python3 
# @title jump-game-ii


from en.Python3.mod.preImport import *
# @test([2,3,1,1,4])=2
# @test([2,3,0,1,4])=2
class Solution:
    def jump(self, nums: List[int]) -> bool:
        """
            Greedy
            Similar to 1326. Minimum Number of Taps to Open to Water a Garden
        """
        n = len(nums)
        ans = 0 # 跳躍次數
        cur = 0 # 當前能跳到的最遠位置
        nxt = 0 # 下一步能跳到的最遠位置

        for i in range(n-1): # 注意不包含終點
            nxt = max(nxt, i + nums[i]) # 更新下一步能跳到的最遠位置
            if i == cur: # 到達當前能跳到的最遠位置
                cur = nxt # 再跳一步
                ans += 1
        return ans