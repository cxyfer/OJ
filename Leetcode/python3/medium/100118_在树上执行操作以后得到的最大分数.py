#
# @lc app=leetcode.cn id=100118 lang=python3
#
# [100118] 在树上执行操作以后得到的最大分数
#


# @lcpr-template-start
import math
from math import *
from typing import *
from collections import *
from functools import *
from itertools import *
from bisect import *
from heapq import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        Tree DP
    """
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        n = len(values)
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        ans = sum(values)

        def dfs(node, parent): # 要保留的節點分數
            if node != 0 and len(g[node]) == 1:
                return values[node]
            ans = values[node] # 保留這個節點的分數，則下面的節點都不用選
            d = 0 # 不保留這個節點的分數，則下面的節點都要選
            for x in g[node]:
                if x != parent:
                    d += dfs(x, node)
            return min(ans, d) # 選/不選，取最小值

        return ans - dfs(0, -1)
# @lc code=end
sol = Solution()
print(sol.maximumScoreAfterOperations([[0,1],[0,2],[0,3],[2,4],[4,5]],[5,2,5,2,1,1])) # 11
print(sol.maximumScoreAfterOperations([[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]],[20,10,9,7,4,3,5])) # 40
