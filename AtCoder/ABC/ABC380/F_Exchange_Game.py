"""
注意到 N + M + L <= 12，因此可以考慮狀壓DP，維護目前手牌以及輪到誰的回合三個狀態。

枚舉當前玩家手牌中可以出的卡，接著可以再選擇不回收任何牌、或再次枚舉牌桌上比打出牌更小的牌回收
如果這些可能中存在任何一種可以使對方贏不了，則自己可以贏；否則就換自己贏不了。
"""

import sys
from functools import cache
sys.setrecursionlimit(10**6)

N, M, L = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

cards = A + B + C

mask = (1 << (N + M + L)) - 1
a = 0
for i in range(N):
    a |= (1 << i)
b = 0
for i in range(N, N + M):
    b |= (1 << i)

# f(a, b, flag) 表示當前輪到某玩家出牌，a 和 b 分別是兩個玩家的手牌，返回某玩家是否能贏
@cache
def f(a, b, flag):
    table = (~(a | b)) & mask # 桌面上的牌是兩個玩家手牌以外的牌

    cur = a if flag else b

    # 當前玩家沒有牌可打就輸了
    if cur == 0:
        return False

    # 枚舉要打出的牌
    for i, x in enumerate(cards):
        if (cur >> i) & 1 == 0:
            continue

        if flag:
            n_a = a & ~(1 << i)
            n_b = b
        else:
            n_a = a
            n_b = b & ~(1 << i)

        n_table = table | (1 << i) # 桌面上的牌加上剛剛打出的牌

        if not f(n_a, n_b, flag ^ 1): # 不回收牌
            return True

        for j, y in enumerate(cards):
            if ((n_table >> j) & 1) and (y < x): # 這張牌在桌面上，且比剛剛打出的牌小，可以回收
                if flag:
                    if not f(n_a | (1 << j), n_b, flag ^ 1):
                        return True
                else:
                    if not f(n_a, n_b | (1 << j), flag ^ 1):
                        return True
    return False

print("Takahashi" if f(a, b, 1) else "Aoki")