"""
Reference:
- https://blog.csdn.net/conti123/article/details/134643350
"""

from collections import defaultdict

def check(x):
    # 檢查狀態是否合法(相鄰兩個1之間至少要有2個0)
    return not (((x >> 2) & x) | (x & (x >> 1)))

n, m = map(int, input().split())
grid = [input() for _ in range(n)]

# 將地圖轉換為二進制表示
g = [0] * (n + 1)
for i in range(n):
    for j in range(m):
        g[i + 1] |= (1 << j) if grid[i][j] == 'H' else 0

# 生成所有合法狀態
states = []
cnt = [0] * (1 << m)
for i in range(1 << m):
    if check(i):
        states.append(i)
        cnt[i] = i.bit_count()

# 預處理相容狀態
compatible = defaultdict(list)
for i in range(len(states)):
    s1 = states[i]
    for j in range(i, len(states)):
        s2 = states[j]
        if not (s1 & s2):  # 兩個狀態不衝突
            compatible[s1].append(s2)
            compatible[s2].append(s1)

# DP
curr = defaultdict(int)
prev = curr.copy()
for i in range(1, n+1):
    curr = defaultdict(int)
    for s in states:
        if g[i] & s:
            continue
        for s1 in compatible[s]:
            if g[i - 1] & s1: # 上一橫列狀態 s1 與地形 g[i-1] 或當前狀態 s 衝突(後者已經預處理)
                continue
            for s2 in compatible[s1]:
                if g[i - 2] & s2 or s & s2: # 上上橫列狀態 s2 與地形 g[i-2] 或當前狀態 s 衝突
                    continue
                curr[(s, s1)] = max(curr[(s, s1)], 
                                    prev[(s1, s2)] + cnt[s])
    prev = curr.copy()

print(max(curr.values()))