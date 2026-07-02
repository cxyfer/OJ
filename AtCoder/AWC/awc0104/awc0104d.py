"""
等差數列差分

e = s + 3d
l              r
s    s+d  s+2d s+3d
s    d    d    d    -e
s    d-s  0    0    -d-e    e
"""


def solve():
    n, m = map(int, input().split())
    T = list(map(int, input().split()))
    P, B = [], []
    for _ in range(m):
        p, b = map(int, input().split())
        P.append(p - 1)
        B.append(b)
    assert len(T) == n and len(P) == m and len(B) == m

    # 等差數列差分
    diff = [0] * (n + 2)

    def add(l, r, s, d):
        if l > r:
            return
        e = s + (r - l) * d
        diff[l] += s
        diff[l + 1] += d - s
        diff[r + 1] += -d - e
        diff[r + 2] += e

    for p, b in zip(P, B):
        l = max(p - b, 0)
        add(l, p, b - (p - l), 1)
        r = min(p + b, n - 1)
        add(p + 1, r, b - 1, -1)

    ans = 0
    s = ss = 0
    for i, t in enumerate(T):
        s += diff[i]
        ss += s
        if ss <= t:
            ans = max(ans, ss)
    print(ans)


if __name__ == "__main__":
    solve()
