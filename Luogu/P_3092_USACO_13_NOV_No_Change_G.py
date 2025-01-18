from collections import defaultdict
from itertools import accumulate
from bisect import bisect_right

K, N = map(int, input().split())
coins = [int(input()) for _ in range(K)]
costs = [int(input()) for _ in range(N)]

tot = sum(coins)
ps = list(accumulate(costs, initial=0))

def find_max_pos(money, start):
    # 建立從 start 開始的每個位置的花費列表
    costs_from_start = [ps[i] - ps[start - 1] for i in range(start, N + 1)]
    # 使用 bisect_right 找出第一個大於 money 的位置
    pos = bisect_right(costs_from_start, money)
    return start + pos - 1

# state: (能買到的位置, 花費)
f = [(0, 0)] * (1 << K)
ans = float('inf')
# 遍歷所有可能的狀態
for curr in range(1, 1 << K):
    for j in range(K):
        if curr & (1 << j):
            prev = curr ^ (1 << j)
            prev_pos, prev_cost = f[prev]
          
            # 計算使用當前硬幣能買到哪裡
            reachable = find_max_pos(coins[j], prev_pos + 1)
            curr_pos, curr_cost = f[curr]
          
            if reachable > curr_pos:
                f[curr] = (reachable, prev_cost + coins[j])
          
            if f[curr][0] == N:
                ans = min(ans, f[curr][1])

print(tot - ans if ans != float('inf') else -1)