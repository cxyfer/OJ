"""
    Prefix Sum + DP

    令 f(k, i) 表示 k 小時後，前 i row 的紅氣球總數，
    則對給定的 [A, B] 區間，答案為 f(k, B) - f(k, A-1)。 (前綴和)。

    觀察可以發現第 k 天的盤面是包含了 3 個前一天的盤面，且右下角的氣球都是藍色的。
    因此不難得出以下性質：
    - 當 i = R 時，f(k, i) = f(k-1, M) * 3，即第 K 天的氣球數是前一天的氣球數的 3 倍。
    - 當 i <= M 時，f(k, i) = f(k-1, i) * 2，前一天的前 i 行的，但包含左右兩邊。
    - 當 i > M 時，f(k, i) = f(k-1, M) * 2 + f(k-1, i-M)，上面的兩塊，以及左下的前 i-M 行。
"""
from functools import cache

@cache
def f(k, i): # f(k, i) 表示 k 小時後，前 i row 的紅氣球總數
    if k == 0: # base case，k=0時，只有第一行有紅氣球
        return 1 if i == 1 else 0
    R, M = 1 << k, 1 << (k-1)
    if i == R: 
        return f(k-1, M) * 3
    if i <= M:
        return f(k-1, i) * 2
    return f(k-1, M) * 2 + f(k-1, i-M)
    
t = int(input())
for kase in range(1, t+1):
    k, a, b = map(int, input().split())
    print(f"Case {kase}: {f(k, b) - f(k, a-1)}")
