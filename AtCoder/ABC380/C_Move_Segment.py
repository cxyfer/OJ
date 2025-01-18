"""
先記錄每個 blocks 的左右端點 [l, r]。

令第 K 個 blocks 左右端點為 [l, r]、第 K - 1 個 blocks 的右端點為 r_prev。
故需要交換的兩段區間分別為 [l, r] 和 [r_prev + 1, l - 1]，直接交換即可。
"""

N, K = map(int, input().split())
S = input()

blocks = []
i = 0
while i < N:
    if S[i] == '1':
        st = i
        while i + 1 < N and S[i + 1] == '1':
            i += 1
        blocks.append((st, i))
    i += 1

r_prev = blocks[K - 2][1]
l, r = blocks[K - 1]
print(S[:r_prev+1] + S[l:r+1] + S[r_prev+1:l] + S[r+1:])