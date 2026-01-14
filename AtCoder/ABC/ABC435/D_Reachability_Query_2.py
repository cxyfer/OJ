def solve():
    n, m = map(int, input().split())

    rg = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(lambda x: int(x) - 1, input().split())
        rg[v].append(u)

    q = int(input())
    vis = set()
    for _ in range(q):
        op, u = map(int, input().split())
        u -= 1
        if op == 1:
            if u in vis:
                continue
            vis.add(u)
            st = [u]
            while st:
                u = st.pop()
                for v in rg[u]:
                    if v not in vis:
                        vis.add(v)
                        st.append(v)
        else:
            print("Yes" if u in vis else "No")

if __name__ == "__main__":
    solve()