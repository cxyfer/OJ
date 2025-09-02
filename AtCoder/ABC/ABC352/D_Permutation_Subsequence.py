"""
    Sliding window
    窗口內是連續的 K 個數字，答案是其中對應的最大座標減最小座標
    Python 需要用 SortedSet 來維護集合中的最大值和最小值
"""
from sortedcontainers import SortedSet

N, K = map(int, input().split())
P = list(map(int, input().split()))
pos = [0] * N # 每個數字對應的位置
for i, p in enumerate(P):
    pos[p-1] = i

st = SortedSet()
for i in range(K-1): # 前 K-1 個數字
    st.add(pos[i])
ans = N
for r in range(K-1, N):
    st.add(pos[r]) # 入窗口，添加右端點的對應座標
    ans = min(ans, st[K-1] - st[0]) # 
    st.remove(pos[r-K+1]) # 出窗口，移除左端點的對應座標
print(ans)