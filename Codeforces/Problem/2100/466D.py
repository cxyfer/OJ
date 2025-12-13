"""
CF466D. Increase Sequence
https://codeforces.com/contest/466/problem/D

# 方法一：組合數學

由於對每個位置，需要的覆蓋數是固定的，因此可以將原陣列轉化為一個新的陣列 B，其中 B[i] = h - A[i]。
如果某個 B[i] < 0，則無解，直接輸出 0。
現在問題轉化為：有多少種合法的區間集合，使得每個位置 i 被覆蓋的次數恰好為 B[i]？

考慮數字之間的間隔，即左括號相當於擺放在數字前面，右括號相當於擺放在數字後面。
由於每種括號在每個位置只能出現一次，因此相鄰兩數之間的擺放方式只有以下 4 種：
1. x    y (不變)
2. x ]  y
3. x  [ y
4. x ][ y

接著考慮相鄰兩數之間的覆蓋數的變化 d = y - x，分為以下幾種情況：
- d = 1: 需要增加一個覆蓋數 -> 必須開啟一個新區間，有 1 種選法，即上述的 3.
- d = -1: 需要減少一個覆蓋數 -> 必須關閉一個舊區間，有 x 種選法，即上述的 2.
- d = 0: 覆蓋數不變，可以什麼都不做，也可以關閉一個舊的，開啟一個新的，有 x + 1 種選法，即上述的 1. 或 4.
- d > 1 或 d < -1: 因為每個位置最多只能開啟一個區間和關閉一個區間，因此無解，直接輸出 

# 方法二：動態規劃

Open and Close Interval Trick
https://codeforces.com/blog/entry/47764

令 f[i][j] 表示考慮到第 i 個數字後，還有 j 個區間處於「開啟」狀態的方案數。
改為考慮每一個數本身，則有以下幾種擺放方式，考慮覆蓋數的變化以及轉移方程：
1.  x  (不操作)
  - 開啟區間數: j -> j (不變)
  - 覆蓋數: j (不變)，因此須滿足 A[i] + j == h
  - 轉移方程: f[i][j] <- f[i-1][j]
2. [x  (開啟一個新區間)
  - 開啟區間數: j - 1 -> j (增加一個區間)
  - 覆蓋數: j - 1 -> j，因此須滿足 A[i] + j == h
  - 轉移方程: f[i][j] <- f[i-1][j-1]
3.  x] (關閉一個舊區間)
  - 開啟區間數: j + 1 -> j (減少一個區間)
  - 覆蓋數: j + 1，因此須滿足 A[i] + j + 1 == h
  - 轉移方程: f[i][j] <- f[i-1][j+1] * (j + 1)  (從 j + 1 個區間中選任意一個關閉)
4. [x] (在該位置放置一個長度為 1 的區間，注意這裡的[]是互相配對的，因此不會增加開啟區間數)
  - 開啟區間數: j -> j (不變)
  - 覆蓋數: j + 1，因此須滿足 A[i] + j + 1 == h
  - 轉移方程: f[i][j] <- f[i-1][j]
5. [x] (關閉一個舊區間，開啟一個新區間，注意這裡的]是和先前的[配對，而[是等待和後面的]配對) 
  - 開啟區間數: j -> j (不變)
  - 覆蓋數: j + 1，因此須滿足 A[i] + j + 1 == h
  - 轉移方程: f[i][j] <- f[i-1][j] * j  (從 j 個區間中選任意一個關閉)
"""
from itertools import pairwise
from collections import defaultdict

MOD = int(1e9 + 7)

def solve1():
    n, h = map(int, input().split())
    A = list(map(int, input().split()))
    assert len(A) == n

    B = [0] + [h - x for x in A] + [0]
    if any(x < 0 for x in B):
        print(0)
        return
    
    ans = 1
    for x, y in pairwise(B):
        diff = y - x
        if diff == 1:
            # 需要增加一個覆蓋數 -> 必須開啟一個新區間，有 1 種選法
            ans = (ans * 1)
        elif diff == -1:
            # 需要減少一個覆蓋數 -> 必須關閉一個舊區間
            # 有 x 個正在進行的區間，可以選任意一個關閉
            ans = (ans * x) % MOD
        elif diff == 0:
            # 覆蓋數不變
            # 選項 1: 什麼都不做，有 1 種選法
            # 選項 2: 關閉一個舊的，開啟一個新的，有 x 種選法
            ans = (ans * (x + 1)) % MOD
        else:
            print(0)
            return
    print(ans)

def solve2():
    n, h = map(int, input().split())
    A = list(map(int, input().split()))
    assert len(A) == n

    if any(x > h for x in A):
        print(0)
        return

    # f[i][j] 表示考慮前 i 個數字後，還有 j 個區間處於「開啟」狀態的方案數。
    f = defaultdict(int)
    f[0] = 1
    for x in A:
        nf = defaultdict(int)

        # A[i] + j == h 的兩種情況：
        # 1. 不操作: f[i][j] <- f[i-1][j]
        # 2. 開啟一個新區間: f[i][j] <- f[i-1][j-1]
        j = h - x
        nf[j] = (f[j] + f[j - 1]) % MOD
        
        # A[i] + j + 1 == h 的三種情況：
        # 3. 關閉一個舊區間: f[i][j] <- f[i-1][j+1] * (j + 1)
        # 4. 在該位置放置一個長度為 1 的區間: f[i][j] <- f[i-1][j]
        # 5. 關閉一個舊區間，開啟一個新區間: f[i][j] <- f[i-1][j] * j
        j = h - x - 1
        nf[j] = (f[j + 1] * (j + 1) + f[j] + f[j] * j) % MOD
        
        f = nf

    print(f[0])

if __name__ == "__main__":
    # solve1()
    solve2()