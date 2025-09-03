from collections import deque

"""
由於每個點最多只有一條出邊，因此只會有以下兩種情況
1. 洽好形成一個或多個環，沒有節點入度為0，用普通 DFS 計算即可
2. 內向基環樹，有若干個入度為0的節點，計算這些點到環的距離哪個最大即可
注意可能存在若干個基環

ZeroJudge 上面的數據不夠強，沒有以下幾種情況：
- 基環樹的樹上有分支
- 有多棵內向基環樹

類題：
- 2127. Maximum Employees to Be Invited to a Meeting 
"""

import sys
input = lambda: sys.stdin.readline().strip()
print = lambda val: sys.stdout.write(str(val) + "\n")

t = int(input())
for kase in range(1, t + 1):
    n = int(input())
    g = [-1] * (n + 1) # 只有一條出邊
    ind = [0] * (n + 1)
    for _ in range(n):
        u, v = map(int, input().split())
        g[u] = v
        ind[v] += 1

    ans = mx = 0
    # 使用拓撲排序建不包含基環的反向圖
    rg = [[] for _ in range(n + 1)]
    q = deque([u for u in range(1, n + 1) if ind[u] == 0])
    while q:
        u = q.popleft()
        v = g[u]
        rg[v].append(u)
        ind[v] -= 1
        if ind[v] == 0:
            q.append(v)

    # 反向圖上 DFS 計算最長鏈長度，以及該條鏈上的葉子節點
    def rdfs(u):
        res, idx = 0, u
        for v in rg[u]:
            cnt, v = rdfs(v)
            if cnt > res or (cnt == res and v < idx):
                res = cnt
                idx = v
        return res + 1, idx

    # 遍歷基環，注意可能有多個基環
    for u in range(1, n + 1):
        if ind[u] == 0: # 略過非基環上的點，或已經訪問過的基環
            continue
        # 找到該基環上的點
        rings = [u] 
        v = g[u]
        while v != u:
            rings.append(v)
            v = g[v]
        # 計算以 v 為根節點的最大鏈長度，以及該條鏈上的葉子節點
        max_len, idx = 0, -1 
        for v in rings:
            ind[v] = 0 # 清空入度，避免重複訪問
            cur_len, cur_idx = rdfs(v)
            if max_len < cur_len or (max_len == cur_len and cur_idx < idx):
                max_len = cur_len
                idx = cur_idx
        # 最大鏈長度加上基環的長度即為此顆基環樹的答案
        max_len += len(rings) - 1 # 減去位於基環上的根節點
        if mx < max_len or (mx == max_len and ans > idx):
            mx = max_len
            ans = idx
    print(f'Case {kase}: {ans}')