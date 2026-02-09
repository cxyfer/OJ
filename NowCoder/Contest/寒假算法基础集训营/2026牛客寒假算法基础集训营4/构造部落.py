"""
B. 构造部落
https://ac.nowcoder.com/acm/contest/120564/B

前綴和
用前綴和維護 [1...x-1] 在位的時間，再加上當前在位的時間 y - 1 即可。
"""
from itertools import accumulate

def solve():
    n, q, s = map(int, input().split())
    A = list(map(int, input().split()))

    ps = [0] + list(accumulate(A))
    for _ in range(q):
        x, y = map(int, input().split())
        print(s + ps[x - 1] + y - 1)

if __name__ == "__main__":
    solve()