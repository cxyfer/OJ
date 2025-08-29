"""
2136A - In the Dream
https://codeforces.com/contest/2136/problem/A

分上下半場考慮，若兩隊的得分分別為 x, y，
則需滿足 min(x, y) * 2 + 2 <= max(x, y)。
"""
def solve():
    a, b, c, d = map(int, input().split())
    c -= a
    d -= b

    if a > b:
        a, b = b, a
    if c > d:
        c, d = d, c
    if b > a * 2 + 2 or d > c * 2 + 2:
        print("NO")
    else:
        print("YES")

t = int(input())
for _ in range(t):
    solve()