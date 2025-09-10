"""
P2625 豪华游轮
https://www.luogu.com.cn/problem/P2625
"""
import math

def solve():
    n = int(input())
    A = [0, 0]
    B = []
    for _ in range(n):
        op, x = input().split()
        x = int(x)
        if op == "forward":
            A[0] += x
        elif op == "backward":
            A[1] += x
        elif op == "left":
            B.append((360 - x) % 360)
        elif op == "right":
            B.append(x % 360)

    m = len(B)
    f = [[False] * 360 for _ in range(2)]
    f[0][0] = True
    for i, x in enumerate(B, 1):
        prev, curr = f[(i - 1) & 1], f[i & 1]
        for v in range(360):
            curr[v] = prev[v] | prev[(v - x) % 360]
    
    ans = A[0] - A[1]
    for d in range(360):
        if f[m & 1][d]:
            # c^2 = a^2 + b^2 - 2ab * cos(C)
            ans = max(ans, math.sqrt(A[0] ** 2 + A[1] ** 2 - 2 * A[0] * A[1] * math.cos(d * math.pi / 180)))
    print(f"{ans:.6f}")  # 四捨五入到小數點後6位

if __name__ == "__main__":
    t = 1
    for _ in range(t):
        solve()