from heapq import heapify, heappop, heappush
from itertools import pairwise

t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input())
    r = list(input())
    pre = [k - 1 if k > 0 else -1 for k in range(n)]
    nxt = [k + 1 if k < n - 1 else -1 for k in range(n)]

    hp = []
    for k, (x, y) in enumerate(pairwise(s)):
        if x != y:
            hp.append(k)
    heapify(hp)

    vis = [False] * n
    flag = True
    for i in range(n - 1):
        while hp:
            k = heappop(hp)
            if k >= n or vis[k]:
                continue
            nk = nxt[k]
            if nk == -1 or vis[nk] or s[k] == s[nk]:
                continue
            s[k] = r[i]
            vis[nk] = True
            nnk = nxt[nk]
            nxt[k] = nnk
            if nnk != -1:
                pre[nnk] = k
            p = pre[k]
            if p != -1 and not vis[p]:
                if s[p] != s[k]:
                    heappush(hp, p)
            if nxt[k] != -1 and not vis[nxt[k]]:
                if s[k] != s[nxt[k]]:
                    heappush(hp, k)
            break
        else:
            flag = False
            break
    print("YES" if flag else "NO")