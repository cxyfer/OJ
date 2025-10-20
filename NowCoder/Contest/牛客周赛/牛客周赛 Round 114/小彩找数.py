"""
A-小彩找数
https://ac.nowcoder.com/acm/contest/119273/A
"""

def solve():
    A = list(map(int, input().split()))
    print(*[A.index(x) + 1 for x in range(1, 4)])

if __name__ == "__main__":
    solve()