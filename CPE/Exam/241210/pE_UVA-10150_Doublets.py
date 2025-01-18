from collections import deque
from string import ascii_lowercase

words = []
line = input().strip()
while line != '':
    words.append(line)
    line = input().strip()

n = len(words)
node2idx = {}
for i, word in enumerate(words):
    node2idx[word] = i

g = [[] for _ in range(n)]
for u, word in enumerate(words):
    for j in range(len(word)):
        c0 = word[j]
        lst = list(word)
        for c in ascii_lowercase:
            if c == c0:
                continue
            lst[j] = c
            v = ''.join(lst)
            if v not in node2idx:
                continue
            v = node2idx[v]
            g[u].append(v)
            g[v].append(u)

queries = []
while True:
    try:
        s, t = input().strip().split()
        queries.append((node2idx[s], node2idx[t]))
    except:
        break

for idx, (s, t) in enumerate(queries):
    vis = [False] * n
    pre = [-1] * n
    q = deque([s])
    vis[s] = True
    while q:
        u = q.popleft()
        if u == t:
            res = []
            while u != -1:
                res.append(words[u])
                u = pre[u]
            res.reverse()
            for word in res:
                print(word)
            break
        for v in g[u]:
            if vis[v]:
                continue
            vis[v] = True
            pre[v] = u
            q.append(v)
    else:
        print('No solution.')

    if idx < len(queries) - 1:
        print()