# @algorithm @lc id=1721 lang=python3 
# @title maximum-profit-of-operating-a-centennial-wheel


from en.Python3.mod.preImport import *
# @test([8,3],5,6)=3
# @test([10,9,6],6,4)=7
# @test([3,4,0,5,1],1,92)=-1
class Solution:
    """
        1. 模擬
    """
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        n = len(customers)
        ans = -1 # 最大利潤所需輪數
        mx = cur = 0 # 最大利潤, 當前利潤
        wait = 0 # 等待人數
        i = 0
        while wait or i < n:
            if i < n:
                wait += customers[i]
            cur += min(4, wait) * boardingCost - runningCost
            wait -= min(4, wait)
            if cur > mx: # 更新最大利潤
                mx = cur
                ans = i + 1
            i += 1
        return ans