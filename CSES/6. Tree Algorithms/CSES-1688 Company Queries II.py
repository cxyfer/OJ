import sys
it = iter(sys.stdin.read().splitlines())
input = lambda: next(it)

def solve():
    n, q = map(int, input().split())
    A = list(map(lambda x: int(x) - 1, input().split()))

    m = n.bit_length()
    # pa[u][i] 表示 u 的第 2^i 個祖先
    pa = [[-1] * m for _ in range(n)]
    dep = [0] * n
    for u, fa in enumerate(A, 1):
        pa[u][0] = fa
        dep[u] = dep[fa] + 1

    # 用倍增法更新 pa
    for i in range(m - 1):
        for u in range(n):
            if pa[u][i] != -1:
                pa[u][i + 1] = pa[pa[u][i]][i]

    def get_kth_ancestor(u: int, k: int) -> int:
        while k and u != -1:
            lb = k & -k
            u = pa[u][lb.bit_length() - 1]
            k &= k - 1
        return u

    def get_lca(u: int, v: int) -> int:
        if dep[u] > dep[v]:
            u, v = v, u
        v = get_kth_ancestor(v, dep[v] - dep[u])
        if v == u:
            return u
        for i in range(m - 1, -1, -1):
            fu, fv = pa[u][i], pa[v][i]
            if fu != fv:  # 同時往上跳 2^i 步後還不會相遇
                u, v = fu, fv
        return pa[u][0]  # 再往上跳一步就是答案

    for i in range(q):
        u, v = map(lambda x: int(x) - 1, input().split())
        print(get_lca(u, v) + 1)
    return

if __name__ == "__main__":
    solve()