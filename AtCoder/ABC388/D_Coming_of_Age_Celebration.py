"""
差分陣列
若 i 給出 g 個石頭，則 [i+1, i+g] 的石頭數量需要增加 1，這可以用差分陣列維護。
對其做前綴和可以得到 i 從前面的人那裡收到的石頭數量 cur。
而根據原本的石頭數量 x 和 cur，以及後面的人數量，可以算出給出的石頭數量 g。
最終答案為 x + cur - g。

時間複雜度為 O(N)。
"""

N = int(input())
A = list(map(int, input().split()))

d = [0] * (N + 1)
ans = [0] * N
cur = 0  # 收到的石頭數量，對差分陣列做前綴和得到
for i, x in enumerate(A):
    cur += d[i]
    give = min(x + cur, N - 1 - i)  # 給出的石頭數量
    if give > 0:
        # 區間 [i + 1, i + give] 的石頭數量增加 1
        d[min(i + 1, N)] += 1
        d[min(i + give + 1, N)] -= 1
    ans[i] = x + cur - give
print(*ans)