"""
D. 东风谷早苗与博丽灵梦
https://ac.nowcoder.com/acm/contest/120564/G
EXGCD
"""

def exgcd(a, b):
    if b == 0:
        return 1, 0, a
    x, y, d = exgcd(b, a % b)
    return y, x - (a // b) * y, d

def solve():
    x, a, s = map(int, input().split())

    x0, y0, g = exgcd(a, s)
    if x % g != 0:
        print("No")
        return

    u0 = x0 * (x // g)
    v0 = y0 * (x // g)
    du = s // g
    dv = a // g

    # u = u0 + du*t >= 0  =>  t >= ceil(-u0/du)
    # v = v0 - dv*t >= 0  =>  t <= floor(v0/dv)
    t_min = -(u0 // du)
    t_max = v0 // dv
    if t_min > t_max:
        print("No")
        return

    # u0 + du*t = v0 - dv*t  =>  (du + dv) * t = v0 - u0
    t_est = (v0 - u0) // (du + dv)

    candidates = set([t_min, t_max])
    for dt in range(-2, 3):
        if t_min <= t_est + dt <= t_max:
            candidates.add(t_est + dt)

    ans = (float('inf'), float('inf'))
    for t in candidates:
        u = u0 + du * t
        v = v0 - dv * t
        if u < 0 or v < 0:
            continue
        if max(u, v) < max(ans[0], ans[1]):
            ans = (u, v)

    if ans == (float('inf'), float('inf')):
        print("No")
        return

    print("Yes")
    print(*ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()