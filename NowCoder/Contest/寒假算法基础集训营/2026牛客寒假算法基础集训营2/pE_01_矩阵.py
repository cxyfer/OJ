"""
E. 01矩阵
https://ac.nowcoder.com/acm/contest/120562/E

神奇構造題
為了方便構造，先猜測是基於對角線對稱的，這樣可以減少一半的構造量。
之後從連通分量數量為 n 想到了之前看過的拼圖 puzzle，於是猜測可以用 n 個 L 形組成。

構造出來的矩陣如下 (n = 7)：
0000000
0111111
0100000
0101111
0101000
0101011
0101010

然後就發現做完了？！
"""
def solve():
    n = int(input())

    ans = [[0] * n for _ in range(n)]
    for i in range(n):
        if i & 1:
            for j in range(i + 1, n):
                ans[i][j] = 1
        for j in range(1, i + 1, 2):
            ans[i][j] = 1

    for row in ans:
        print(*row, sep='')

if __name__ == "__main__":
    solve()