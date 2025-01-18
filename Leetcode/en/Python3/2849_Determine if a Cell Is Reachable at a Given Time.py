# @algorithm @lc id=3056 lang=python3 
# @title determine-if-a-cell-is-reachable-at-a-given-time


# from en.Python3.mod.preImport import *
from typing import List
# @test(2,4,7,7,6)=true
# @test(3,1,7,3,3)=false
# @test(1, 1, 1, 1, 3)=true
# @test(1, 1, 1, 3, 2)=true
# @test(1, 1, 2, 1, 2)=true
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        # 精簡版
        minStep = abs(sx - fx) + abs(sy - fy) - min(abs(sx - fx), abs(sy - fy))
        return False if (minStep > t) or (sx==fx and sy==fy and t-minStep==1) else True
    
        # 周賽時寫的
        if minStep > t:
            return False
        if minStep == t:
            return True
        # 再來考慮增加步數的方法
        diffStep = t - minStep
        if diffStep > 1: # 因為必有兩步、三步的增加步數方法(繞圈圈)，所以只要大於1就一定可以
            return True
        else:
            if min(abs(sx - fx), abs(sy - fy)) > 0: # 走一步斜的改成走兩步直的
                return True
            elif abs(sx - fx) > 0 or abs(sy - fy) > 0: # 走一步直的改成走兩步斜的
                return True
            else:
                return False


sol = Solution()
print(sol.isReachableAtTime(2,4,7,7,6)) # true
print(sol.isReachableAtTime(3,1,7,3,3)) # false
print(sol.isReachableAtTime(1, 1, 1, 1, 3)) # true
print(sol.isReachableAtTime(1, 1, 1, 3, 2)) # true
print(sol.isReachableAtTime(1, 1, 2, 1, 2)) # true