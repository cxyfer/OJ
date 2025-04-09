"""
單調佇列優化 DP

令 f[i] 表示前 i 頭奶牛可以獲得的最效率
則可以枚舉上一頭休息的牛 j 的位置，得
f[i] = max(f[j-1] + sum(E[j+1]...E[i])), for j in [i - k, i]
     = max(f[j-1] + s[i] - s[j]), for j in [i - k, i]
     = s[i] + max(f[j-1] - s[j]), for j in [i - k, i]
可以用單調佇列來維護 f[j-1] - s[j] 的值
"""

from collections import deque

n, k = map(int, input().split())
E = [0] + [int(input()) for _ in range(n)]

s = [0] * (n + 1)
for i in range(1, n + 1):
    s[i] = s[i - 1] + E[i]

f = [0] * (n + 1)  # 定義 f[-1] = 0
w = [0] * (n + 1)  # w[j] = f[j-1] - s[j], w[0] = f[-1] - s[0] = 0

q = deque([0])  # 單調遞減佇列
for i in range(1, n + 1):
    # 1. 由於轉移時包含當前位置，故需要先計算 w[i]
    w[i] = f[i-1] - s[i]
    while q and w[q[-1]] <= w[i]:
        q.pop()
    q.append(i)

    # 2. 刪除不在窗口範圍 [max(0, i-K), i] 內的索引
    while q and q[0] < i - k:
        q.popleft()
    
    # 3. 根據單調佇列中保存的最大值計算 f[i]
    # f[i] = s[i] + max(f[j-1] - s[j]), for j in [i - k, i]
    f[i] = s[i] + w[q[0]]

print(f[n])