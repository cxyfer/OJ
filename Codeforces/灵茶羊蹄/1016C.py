"""
路徑只有三種可能：
1. 直接向右走
    01 02 03 04 05 06
    12 11 10 09 08 07
2. 一直上下走
    01 04 05 08 09 12
    02 03 06 07 10 11
3. 先上下走，之後向右走
    01 04 05 06 07 08
    02 03 12 11 10 09
以上三種可能可以合併成一種，就是先上下走，之後向右走，可以枚舉何時開始向右走
"""

from itertools import accumulate

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

s1 = list(accumulate(A, initial=0))
s2 = list(accumulate(B, initial=0))

# f1[i] 表示從 (1, i) 開始向右走的總和
# f2[i] 表示從 (2, i) 開始向右走的總和
f1 = [0] * (n + 1)
f2 = [0] * (n + 1)

for i in range(n - 1, -1, -1):
    # 減去從 i+1 到 n 的 A 和 B 的累積和，加上當前點的貢獻
    f1[i] = f1[i + 1] - (s1[n] - s1[i + 1]) - (s2[n] - s2[i + 1]) + 2 * i * A[i] + (2 * n - 1) * B[i]
    f2[i] = f2[i + 1] - (s1[n] - s1[i + 1]) - (s2[n] - s2[i + 1]) + 2 * i * B[i] + (2 * n - 1) * A[i]

ans = f1[0]  # 直接向右走的總和
cur = 0  # 一直上下走的總和
for i, (a, b) in enumerate(zip(A, B)):
    if i & 1:  # 此時可以從第一橫列開始向右走
        cur += 2 * i * b + (2 * i + 1) * a
        ans = max(ans, cur + f1[i + 1])
    else:  # 此時可以從第二橫列開始向右走
        cur += 2 * i * a + (2 * i + 1) * b
        ans = max(ans, cur + f2[i + 1])
print(ans)