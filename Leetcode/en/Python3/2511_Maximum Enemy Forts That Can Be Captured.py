# @algorithm @lc id=2602 lang=python3 
# @title maximum-enemy-forts-that-can-be-captured


from en.Python3.mod.preImport import *
# @test([1,0,0,-1,0,0,0,0,1])=4
# @test([0,0,1,-1])=0
class Solution:
    def captureForts(self, forts: List[int]) -> int:
        ans = 0
        left = -1 # 表示上個我方城堡或空地的位置
        for idx, fort in enumerate(forts):
            if fort == -1 or fort == 1: # 遇到我方城堡或空地
                if left != -1 and forts[left] != fort: # 空地->我方城堡 或 我方城堡->空地
                    ans = max(ans, idx - left - 1) # 中間都是敵方城堡
                left = idx
        return ans