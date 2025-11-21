#
# @lc app=leetcode id=757 lang=python3
#
# [757] Set Intersection Size At Least Two
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
Greedy

當我們發現一個不滿足條件的區間時，應該貪心地選擇能夠使後續區間滿足條件的數字。
故先將區間按照 ed 從小到大排序，然後維護兩個指針 p1 和 p2，代表目前選取集合中最大的兩個數字，且保持 p1 < p2
需要注意的是，對於 ed 相同的區間，需要按照 st 從大到小排序

則有以下幾種情況：
1. p1 和 p2 都在區間內，則無需新增
2. 只有 p2 在區間內，p1 在區間外，則需要新增 1 個點。為了貪婪地覆蓋後續區間，選擇當前區間的最大值 e
3. p1 和 p2 都不在區間內，則需要新增 2 個點。貪婪選擇當前區間最大的兩個值 e-1 和 e
"""
# @lc code=start
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        p1, p2 = -1, -1  # 代表目前選取集合中最大的兩個數字，且保持 p1 < p2
        ans = 0
        for st, ed in intervals:
            if st <= p1:  # 1. p1 和 p2 都在區間內
                continue
            elif st <= p2:  # 2. 只有 p2 在區間內，p1 在區間外
                p1, p2 = p2, ed
                ans += 1
            else:  # 3. p1 和 p2 都不在區間內
                ans += 2
                p1, p2 = ed - 1, ed
        return ans
# @lc code=end

sol = Solution()
print(sol.intersectionSizeTwo([[1,3],[3,7],[8,9]]))  # 5
print(sol.intersectionSizeTwo([[1,3],[3,7],[5,7],[7,8]]))  # 5
