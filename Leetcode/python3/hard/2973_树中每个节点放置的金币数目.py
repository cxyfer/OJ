#
# @lc app=leetcode.cn id=2973 lang=python3
#
# [2973] 树中每个节点放置的金币数目
#
from preImport import *
# @lc code=start
class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        n = len(cost)
        g = defaultdict(list)
        for u, v in edges: # 無向圖
            g[u].append(v)
            g[v].append(u)
        ans = [1] * n # 初始化答案為1，即子樹中傑點數量 < 3 的情況

        def smallest3(hp): # 返回 Min Heap 的前三小元素
            n = len(hp)
            if n <= 2:
                return hp
            if n == 3:
                return hp if hp[1] < hp[2] else [hp[0], hp[2], hp[1]]
            res = [hp[0]]
            if hp[1] < hp[2]:
                res.append(hp[1])
                x = hp[3] if n > 3 else 0
                y = hp[4] if n > 4 else 0
                res.append(min(hp[2], min(x, y)))
            else:
                res.append(hp[2])
                x = hp[5] if n > 5 else 0
                y = hp[6] if n > 6 else 0
                res.append(min(hp[1], min(x, y)))
            return res
        
        def dfs(u, fa):
            res = 1 # 子樹中的節點數量
            hp1 = [-cost[u]] if cost[u] > 0 else [] # 正數，MaxHeap
            hp2 = [cost[u]] if cost[u] <= 0 else [] # 負數，MinHeap
            for v in g[u]:
                if v != fa:
                    x, res_hp1, res_hp2 = dfs(v, u)
                    res += x
                    hp1.extend(res_hp1)
                    hp2.extend(res_hp2)
            # Heap
            heapify(hp1) # O(n)
            heapify(hp2) # O(n)
            hp1 = sorted(hp1[:7])[:3] # 只取前3大正數，取前3層做排序
            hp2 = sorted(hp2[:3])[:2] # 只取前2小負數，取前2層做排序
            # 排序
            # hp1 = sorted(hp1)[:3] # 只取前3大正數
            # hp2 = sorted(hp2)[:2] # 只取前2小負數
            if res >= 3:
                tmp1 = tmp2 = float('-inf')
                if len(hp1) >= 3: # 三正
                    tmp1 = -hp1[0] * -hp1[1] * -hp1[2]
                if len(hp1) >= 1 and len(hp2) >= 2: # 一正兩負
                    tmp2 = -hp1[0] * hp2[0] * hp2[1]
                ans[u] = max(0, tmp1, tmp2) # 剩餘情況都是負數，根據題意，放0
            return res, hp1, hp2
        dfs(0, -1)
        return ans
# @lc code=end

