t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    c = 1
    ans = []
    st = set()
    for u, v in edges:
        if u == c or v == c:
            d = v if u != c else u
            for nc in range(1, n+1):
                if nc != d and nc != c:
                    c = nc
                    break
        ans.append((u, v, c))
        for node in [u, v]:
            if node in st:
                st.remove(node)
            else:
                st.add(node)
    st = list(st)
    idx = 0
    while idx + 1 < len(st):
        u = st[idx]
        v = st[idx + 1]
        ans.append((u, v, c))
        idx += 2
    if idx < len(st):
        u = st[idx]
        d = u % n + 1
        if d == c or d == u:
            d = (d % n) + 1
        if d == c or d == u:
            d = (d % n) + 1
        ans.append((u, c, d))
    print(len(ans))
    for op in ans:
        print(f"{op[0]} {op[1]} {op[2]}")