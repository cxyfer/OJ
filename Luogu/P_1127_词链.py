"""
由於連接兩個單字的條件是 前一個單字的尾字母 與 後一個單字的頭字母 相同，
因此可以將這個相同的字母視為頂點，將連接兩個單字轉換為連接同一個單字頭尾字母的邊，
即將 a...b -> b...c，轉換為 a -> b -> c，這樣就轉換為 歐拉路徑 問題。
"""

from collections import defaultdict

n = int(input())
words = [input().strip() for _ in range(n)]
words.sort()  # 按字典序排序

g = [[] for _ in range(26)]
deg = [0] * 26
for idx, word in enumerate(words):
    st = ord(word[0]) - ord('a')
    ed = ord(word[-1]) - ord('a')
    g[st].append((ed, idx))  # 存這條邊對應的單字索引
    deg[st] += 1
    deg[ed] -= 1

st = -1
for i in range(26):
    if deg[i] == 1:
        st = i
        break
else:
    st = ord(words[0][0]) - ord('a')

used = [False] * n  # 標記單字(邊)是否使用過
path = []
def dfs(u):
    while g[u]:
        v, idx = g[u].pop(0) # 從字典序較小的單字(邊)開始
        if used[idx]:
            continue
        used[idx] = True
        dfs(v)
        path.append(idx)
dfs(st)

if len(path) != n: # 形成的詞鏈不包含所有單字
    print("***")
else:
    path = path[::-1]
    print('.'.join(words[idx] for idx in path))