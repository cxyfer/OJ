"""
首先考慮有解的情況：
假設第 i 個位置的石頭來源是 from_i，則移動的距離為 i - from_i，
總距離為 sum(i - from_i) = sum(i) - sum(from_i)，
其中 sum(i) = n * (n + 1) // 2，
而 sum(from_i) 即原本石頭位置的和，為 sum(X_i * A_i for X_i, A_i in stones)。

接著考慮無解的情況：
- 由於最後石頭的數量必須為 n，因此只要 sum(A) != n 即無解。
- 由於石頭只能往後移動，因此我們可以模擬移動的過程，只要中途數量出現負數即無解。
    - 但如果枚舉每個位置顯然會超時，但我們其實只需要枚舉存在石頭的位置即可。
    - 在這個過程中維護多餘的石頭數量 cur、上一個石頭的位置 last。
"""
n, m = map(int, input().split())
X = list(map(int, input().split())) # 位置
A = list(map(int, input().split())) # 數量

stones = sorted(zip(X, A), key=lambda x: x[0]) # 按位置排序
ans = n * (n + 1) // 2 - sum(pos * val for pos, val in stones)
if sum(A) != n:
    ans = -1
cur = 0 # 多餘的石頭數量
last = 0 # 上一個石頭的位置
for pos, val in stones:
    cur -= (pos - (last + 1)) # [last + 1, pos - 1] 都需要石頭
    if cur < 0:
        ans = -1
        break
    cur += val - 1 # 留一個給自己
    last = pos
cur -= (n - last) # [last + 1, n] 也都需要石頭
if cur != 0:
    ans = -1
print(ans)