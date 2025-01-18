#
# @lc app=leetcode.cn id=1744 lang=python3
#
# [1744] 你能在你最喜欢的那天吃到你最喜欢的糖果吗？
#
from preImport import *
# @lc code=start
class Solution:
    """
        Prefix Sum + Reading Test

        https://leetcode.cn/problems/can-you-eat-your-favorite-candy-on-your-favorite-day/solutions/806205/gong-shui-san-xie-qian-zhui-he-qiu-jie-c-b38y
    """
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        s = list(accumulate(candiesCount, initial=0))
        ans = []
        # print("Prefix Sum:", s)
        for t, d, c in queries: # a, b: 1-based; d: 0-based
            a = s[t] // c + 1# 每天都吃 c 顆，最快第 a 天能吃到 Type t 的糖果
            b = s[t+1] # 一天吃一顆，最慢第 b 天能吃到 Type t 的糖果
            # print(t, d, c, a, b, sep="\t")
            ans.append(a <= d+1 <= b) # convert 0-based to 1-based
        return ans
# @lc code=end
sol = Solution()
print(sol.canEat([7,4,5,3,8], [[0,2,2],[4,2,4],[2,13,1000000000]])) # [True,False,True]
print(sol.canEat([5,2,6,4,1], [[3,1,2],[4,10,3],[3,10,100],[4,100,30],[1,3,1]])) # [False,True,True,False,False]