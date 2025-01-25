"""
在一個 n x m 的矩形中，邊長為 k 的正方形的數量可以表示為：
S_k = (n - k + 1) * (m - k + 1)
其中 k 的範圍是 1 <= k <= min(n, m)

令 c = min(n, m)，d = max(n, m)
故總的正方形數量為：
S = sum(S_k) for k in range(1, min(n, m) + 1)
  = sum((c - k + 1) * (d - k + 1)) for k in range(1, c + 1)

展開上式後可以得到：
S = d * c * (c + 1) / 2 - c * (c + 1) * (c - 1) / 6

將 S = x 代入，則對於已知的 x 和 c，我們可以求出 d
d = (6x + c^3 - c) / (3c(c + 1))

遍歷 c 時可以考慮 c 的範圍，由於 c <= d = (6x + c^3 - c) / (3c(c + 1))
化簡後得到 6x >= 2c^3 + 3c^2 + c
可以忽略低次項，得到 6x ~= 2c^3，同時開立方根後得到 c ~= 1/2 * (6x)^(1/3)
為了保險起見，可以將 c 的範圍設為 1 <= c <= (6x)^(1/3) + 2
"""

x = int(input())
ans = []
max_c = int((6 * x) ** (1/3)) + 2  # 上限設為大約 (6x)^(1/3)
for c in range(1, max_c + 1): # 枚舉所有可能的 c = min(n, m)
    numerator = 6 * x + c**3 - c
    denominator = 3 * c * (c + 1)
    if numerator % denominator != 0:
        continue
    d = numerator // denominator
    if d < c:  # d = max(n, m) 必須大於 c
        continue
    ans.append((c, d))
    if c != d:
        ans.append((d, c))
print(len(ans))
for x, y in sorted(ans):
    print(x, y)