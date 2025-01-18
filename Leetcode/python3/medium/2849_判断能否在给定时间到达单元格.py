#
# @lc app=leetcode.cn id=2849 lang=python3
#
# [2849] 判断能否在给定时间到达单元格
#

# @lc code=start
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
# @lc code=end

