"""
2134A - Painting With Two Colors
https://codeforces.com/contest/2134/problem/A
構造

只有當 a, b 的奇偶性與 n 的奇偶性相同時，才能滿足條件，
但由於 b 可以把 a 蓋住，因此當 b >= a 時，a 的奇偶性不重要
"""

def solve():
    n, a, b = map(int, input().split())
    if n & 1 == a & 1 == b & 1 or n & 1 == b & 1 and b >= a:
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    solve()