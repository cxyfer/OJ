# @algorithm @lc id=2257 lang=python3 
# @title earliest-possible-day-of-full-bloom


from en.Python3.mod.preImport import *
# @test([1,4,3],[2,3,1])=9
# @test([1,2,3,2],[2,1,2,1])=9
# @test([1],[1])=2
class Solution:
    """
        Greedy
        plantTime的總和是固定的，因此貪婪的思路是盡可能先種growTime長的花
    """
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        ans = 0
        cur = 0 # 當前時間
        for pt, gt in sorted(zip(plantTime, growTime), key=lambda x:x[1], reverse=True):
            cur += pt # 種植完成的時間
            ans = max(ans, cur + gt) # 若當前花開的時間比答案還晚，則更新答案
        return ans