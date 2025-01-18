n = int(input())

g = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(lambda x: int(x) - 1, input().split())
    g[u].append(v)
    g[v].append(u)

ans = 0
used = [False] * n
st = [(0, -1, True)]
while st:
    u, fa, flag = st.pop()
    if flag:
        st.append((u, fa, False))
        for v in g[u]:
            if v == fa:
                continue
            st.append((v, u, True))
    else:
        for v in g[u]:
            if v == fa:
                continue
            if not used[v] and not used[u]:
                ans += 1
                used[u] = used[v] = True
                break
print(ans)