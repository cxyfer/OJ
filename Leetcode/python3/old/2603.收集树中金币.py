#
# @lc app=leetcode.cn id=2603 lang=python3
#
# [2603] 收集树中金币
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    """
        兩次Topological sort
        1. 去除沒有金幣的葉子，第一次Topological sort
        2. 根據題目條件，去除到葉子距離 < 2 的節點，第二次Topological sort
        3. 剩餘的點都是必須要訪問的點，所以答案就是剩餘的邊數 * 2
        - https://www.bilibili.com/video/BV11o4y1p7Ci
    """
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        graph = [[] for _ in range(n)]
        degrees = [0] * n # degree of each node
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degrees[u] += 1
            degrees[v] += 1
        # degrees = list(map(len, graph)) 

        left_edges = n - 1 # 剩餘的邊數
        # Topological sort，去掉沒有金幣的葉子
        q = deque()
        for idx, (deg, coin) in enumerate(zip(degrees, coins)):
            if deg == 1 and coin == 0: # 沒有金幣的葉子
                q.append(idx)
        while q:
            left_edges -= 1  # 刪除該葉子到其父節點的邊
            cur = q.popleft()
            for y in graph[cur]: 
                degrees[y] -= 1
                if degrees[y] == 1 and coins[y] == 0: # 其父節點變成沒有金幣的葉子
                    q.append(y)

        # 再次 Topological sort，去掉有金幣的葉子
        for idx, (deg, coin) in enumerate(zip(degrees, coins)):
            if deg == 1 and coin > 0: # 有金幣的葉子
                q.append(idx)
        left_edges -= len(q)  # 刪除所有有金幣的葉子（到其父節點的邊）
        for x in q: # 遍歷所有有金幣的葉子
            for y in graph[x]:
                degrees[y] -= 1
                if degrees[y] == 1: # y 變成葉子
                    left_edges -= 1  # 刪除 y 到其父節點的邊
        return max(left_edges * 2, 0) # 一個金幣都沒有的情況，left_edges = (n -1) - n = -1，所以要取 max(0, left_edges * 2)

# @lc code=end

