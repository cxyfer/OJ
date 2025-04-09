---
title: P2627 [USACO11OPEN] Mowing the Lawn G
source: https://www.luogu.com.cn/problem/P2627
created: 2025-04-09
tags:
  - OnlineJudge
  - Luogu
  - 動態規劃
  - 單調佇列
  - 單調佇列優化DP
---
# P2627 [USACO11OPEN] Mowing the Lawn G

在一年前赢得了小镇的最佳草坪比赛后，Farmer John 变得很懒，再也没有修剪过草坪。现在，新一轮的最佳草坪比赛又开始了，Farmer John 希望能够再次夺冠。

然而，Farmer John 的草坪非常脏乱，因此，Farmer John 只能够让他的奶牛来完成这项工作。Farmer John 有 $N$（$1\le N\le 10^5$）只排成一排的奶牛，编号为 $1\ldots N$。每只奶牛的效率是不同的，奶牛 $i$ 的效率为 $E_i$（$0\le E_i\le 10^9$）。

靠近的奶牛们很熟悉，因此，如果 Farmer John安排超过 $K$ 只连续的奶牛，那么，这些奶牛就会罢工去开派对 :)。因此，现在 Farmer John 需要你的帮助，计算 FJ 可以得到的最大效率，并且该方案中没有连续的超过 $K$ 只奶牛。

## 输入格式

第一行：空格隔开的两个整数 $N$ 和 $K$。

第二到 $N+1$ 行：第 $i+1$ 行有一个整数 $E_i$。

## 输出格式

第一行：一个值，表示 Farmer John 可以得到的最大的效率值。

## 输入输出样例 #1

### 输入 #1

```
5 2
1
2
3
4
5
```

### 输出 #1

```
12
```

---

## 思路：單調佇列優化 DP

設 $f[i]$ 表示前 $i$ 頭奶牛最多能獲得的總效率，那麼我們可以決定上一頭休息的奶牛的位置 $j$，使得 $j$ 滿足：
- $i - k \leq j \leq i$，即兩頭被選奶牛之間最多間隔 $k$ 頭奶牛（題目條件）
- $j$ 可以等於 $i$，表示休息的奶牛是第 $i$ 頭奶牛

則狀態轉移方程為：
$$
f[i] = \max_{j = i - k}^{i} \left( f[j - 1] + \sum_{t = j+1}^{i} E_t \right)
$$
其中，$E_t$ 表示第 $t$ 頭奶牛的效率。

為了方便計算區間和，定義前綴和：
$$
s[i] = \sum_{t=1}^{i} E_t
$$

則狀態轉移可以改寫為：
$$
f[i] = \max_{j = i - k}^{i} \left( f[j - 1] + s[i] - s[j] \right)
$$

進一步整理，得到：
$$
f[i] = s[i] + \max_{j = i - k}^{i} \left( f[j - 1] - s[j] \right)
$$

### 單調佇列優化

注意到查詢區間隨著 $i$ 遞增「向右平移」，且要求在每個 $i$ 求 $\max (f[j-1] - s[j])$（定義為 $w[j]$），因此我們可以利用單調佇列技巧來動態維護一個遞減序列以便在 $O(1)$ 時間內取得區間內最大值，整體時間複雜度降低至 $O(n)$。

### 注意事項

按照此定義，當 $j = 0$ 時，需要考慮 $f[-1] - s[0]$，會出現下標越界，這裡的處理方式是定義 $w[j] = f[j-1] - s[j]$，並且定義 $w[0] = 0$，這樣可以保證 $w[j]$ 的定義在 $j = 0$ 時是合法的。

---

## Code

```python
from collections import deque

n, k = map(int, input().split())
E = [0] + [int(input()) for _ in range(n)]

s = [0] * (n + 1)
for i in range(1, n + 1):
    s[i] = s[i - 1] + E[i]

f = [0] * (n + 1)  # 定義 f[-1] = 0
w = [0] * (n + 1)  # w[j] = f[j-1] - s[j], w[0] = f[-1] - s[0] = 0

q = deque([0])  # 單調遞減佇列
for i in range(1, n + 1):
    # 1. 由於轉移時包含當前位置，故需要先計算 w[i]
    w[i] = f[i-1] - s[i]
    while q and w[q[-1]] <= w[i]:
        q.pop()
    q.append(i)

    # 2. 刪除不在窗口範圍 [max(0, i-K), i] 內的索引
    while q and q[0] < i - k:
        q.popleft()
    
    # 3. 根據單調佇列中保存的最大值計算 f[i]
    # f[i] = s[i] + max(f[j-1] - s[j]), for j in [i - k, i]
    f[i] = s[i] + w[q[0]]

print(f[n])
```