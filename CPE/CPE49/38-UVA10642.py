"""
    CPE49 的測資又又又有問題了
"""

import sys
buf = sys.stdin.read().split()
cin = lambda: buf.pop(0)

# T = int(input())
T = int(cin())

def calc(x, y): # from (0, 0) to (x, y)
    t = x + y
    return (t-1) * (t) // 2 + t + x

for tc in range(1, T+1):
    # sx, sy, ex, ey = map(int, input().split()) 
    sx, sy, ex, ey = map(int, [cin() for _ in range(4)])
    print(f"Case {tc}: {calc(ex, ey) - calc(sx, sy)}")