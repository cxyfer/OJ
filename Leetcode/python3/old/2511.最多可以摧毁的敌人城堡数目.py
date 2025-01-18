#
# @lc app=leetcode.cn id=2511 lang=python3
#
# [2511] 最多可以摧毁的敌人城堡数目
#
from en.Python3.mod.preImport import *
# @lc code=start
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
# @lc code=end

