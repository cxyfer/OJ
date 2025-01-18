#
# @lc app=leetcode.cn id=401 lang=python3
#
# [401] 二进制手表
#
from en.Python3.mod.preImport import *
# @lc code=start
"""
    Backtracking
    similar to 46.Permutations.
    similar to 51.N queens
"""
class Solution1:
    """
        模板化的寫法，要過濾掉重複的組合
        Similar to 216.Combination Sum III
    """
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        res = []
        times = [ 1 << i for i in range(6)] + [ 100 * 1 << i for i in range(4)] # 嚴格遞增
        def check(t):
            return False if (t % 100 > 59) or (t // 100 > 11) else True
        def backtrace(i: int, avail: set) -> None:
            t = sum(res)
            if not check(t):
                return
            if i == turnedOn:
                ans.append(f"{t // 100}:{t % 100:02d}")
                return
            for num in avail:
                res.append(num)
                # 這裡要過濾掉比num小的數字，因為這樣才能保證不重複
                backtrace(i + 1, set([x for x in avail if x > num]))
                res.pop()
        backtrace(0, set(times))
        return ans
class Solution2:
    """
        因為是取組合，所以可以用下標來避免重複，不用額外的set，但要另外檢查是否到達目的長度
    """
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        times = [ 100 * 1 << i for i in range(4)] + [ 1 << i for i in range(6)] 
        def check(t):
            return False if (t % 100 > 59) or (t // 100 > 11) else True
        def backtrace(num: int, s: int, t:int) -> None:
            if not check(t):
                return
            if num == turnedOn:
                ans.append(f"{t // 100}:{t % 100:02d}")
                return
            for i in range(s, 10):
                backtrace(num + 1 ,i + 1, t + times[i])
        backtrace(0, 0, 0)
        return ans
class Solution(Solution2):
    ...
# @lc code=end
sol = Solution()
# print(sol.readBinaryWatch(1))
print(sol.readBinaryWatch(9))
# print(sol.readBinaryWatch(4))