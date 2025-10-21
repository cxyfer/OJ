"""
C - 仰望水面的歪
https://ac.nowcoder.com/acm/problem/280263
"""

import sys
import math
input = sys.stdin.readline

def solve():
    n, h = map(int, input().split())
    for _ in range(n):
        x, y, z = map(int, input().split())
        z += 2 * (h - z)
        g = math.gcd(x, math.gcd(y, z))
        print(x // g, y // g, z // g)

if __name__ == '__main__':
    solve()