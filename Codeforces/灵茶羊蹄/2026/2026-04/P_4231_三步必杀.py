"""
P4231 三步必杀
https://www.luogu.com.cn/problem/P4231
等差數列差分模板題

e = s + 3d
l              r
s    s+d  s+2d s+3d
s    d    d    d    -e
s    d-s  0    0    -d-e    e
"""


def solve():
    n, m = map(int, input().split())

    diff = [0] * (n + 3)

    for _ in range(m):
        l, r, s, e = map(int, input().split())
        d = (e - s) // (r - l)
        diff[l] += s
        diff[l + 1] += d - s
        diff[r + 1] += -d - e
        diff[r + 2] += e

    mx, xor = 0, 0
    s = ss = 0
    for i in range(1, n + 1):
        s += diff[i]
        ss += s
        mx = max(mx, ss)
        xor ^= ss

    print(xor, mx)


if __name__ == "__main__":
    solve()
