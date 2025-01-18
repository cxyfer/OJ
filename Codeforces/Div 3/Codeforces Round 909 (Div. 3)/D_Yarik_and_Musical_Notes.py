"""
bi = 2 ^ ai
求滿足 bi ^ bj = bj ^ bi 的數對 (i, j) 的數量
=> (2^ai) ^ (2^aj) = (2^aj) ^ (2^ai)
=> 2^(ai*2^aj) = 2^(aj*2^ai)
=> ai*2^aj = aj*2^ai
=> 2^(aj - ai) = aj / ai
=> aj / ai 是 2 的冪次方
=> ai = aj 或 ai = 1, aj = 2 或 ai = 2, aj = 1
"""
import sys
from collections import defaultdict

input = sys.stdin.readline
print = sys.stdout.write

T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0
    cnt = defaultdict(int)
    cnt[1] = cnt[2] = 0 # 不加這行會 TLE

    for val in A:
        ans += cnt[val] # ai = aj
        if val == 1: # ai = 2, aj = 1
            ans += cnt[2]
        elif val == 2: # ai = 1, aj = 2
            ans += cnt[1]
        cnt[val] += 1
    print(f"{ans}\n")

