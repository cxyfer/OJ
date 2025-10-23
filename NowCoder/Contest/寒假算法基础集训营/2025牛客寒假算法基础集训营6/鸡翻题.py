"""
K - 鸡翻题
https://ac.nowcoder.com/acm/contest/95338/K

在若干次翻頁後，朝上的兩頁分別是 x + 2k 和 x + 1 + 2k
欲使 y = 2x + 4k + 1 成立，則 y - (2x + 1) 必須是 4 的倍數
"""
t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    if (y - 2 * x - 1) % 4 == 0:
        print("YES")
    else:
        print("NO")