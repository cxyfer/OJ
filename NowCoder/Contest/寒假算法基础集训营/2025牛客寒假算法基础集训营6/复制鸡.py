"""
A - 复制鸡
https://ac.nowcoder.com/acm/contest/95338/A

根據題意，每一段連續的相同數字最少需要由一個初始數字複製而成。
故所求答案為連續相同數字的段數。
"""
from itertools import groupby

def solve():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n

    print(len(list(groupby(A))))

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()