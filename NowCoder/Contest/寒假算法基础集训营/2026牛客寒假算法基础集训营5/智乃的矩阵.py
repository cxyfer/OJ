"""
H. 智乃的矩阵
https://ac.nowcoder.com/acm/contest/120565/H

注意到有兩個基本性質：
1. 只有當總和可以被 n^2 整除時，才有可能均分為 n^2 個相同的數 tgt。
2. 黑白染色後，操作時不會改變相同顏色格子的總和，因此也需要檢查黑白格子的總和是否可以均分，且平均值相同。

疊加兩次操作後，可以得到如下矩陣：
[[2, 0],
 [0, -2]]
這意味這相同顏色的格子之間可以每次移動 2 個單位，這意味著只有和 tgt 同奇偶的格子才有可能變成 tgt。

然而對於一次操作，可以改變 4 個格子的奇偶性，因此我們可以在遇到奇偶性不符的格子時，對其所在的 2x2 區域進行操作。
最後檢查所有格子的奇偶性是否和 tgt 相同即可。
"""
def solve():
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]

    if n == 1:
        print("Yes")
        return

    # 1. 檢查是否可以均分為 n^2 個相同的數
    m = n * n
    tot = sum(map(sum, grid))
    if tot % m:
        print("No")
        return
    tgt = tot // m

    # 2. 檢查黑白格子的總和是否可以均分，且平均值相同
    s = [0, 0]
    cnt = [0, 0]
    for i, row in enumerate(grid):
        for j, x in enumerate(row):
            s[(i + j) & 1] += x
            cnt[(i + j) & 1] += 1

    if s[0] % cnt[0] or s[1] % cnt[1] or s[0] // cnt[0] != tgt or s[1] // cnt[1] != tgt:
        print("No")
        return

    # 3. 檢查奇偶性是否符合 tgt，若不符合則對其所在的 2x2 區域進行操作。
    for i, row in enumerate(grid):
        for j, x in enumerate(row):
            grid[i][j] = x & 1
    tgt = tgt & 1

    for i in range(n - 1):
        for j in range(n - 1):
            if grid[i][j] != tgt:
                grid[i][j] ^= 1
                grid[i][j + 1] ^= 1
                grid[i + 1][j] ^= 1
                grid[i + 1][j + 1] ^= 1

    # 4. 檢查剩餘格子的奇偶性是否和 tgt 相同。
    if all(grid[i][n - 1] == tgt for i in range(n)) and all(grid[n - 1][j] == tgt for j in range(n)):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    solve()