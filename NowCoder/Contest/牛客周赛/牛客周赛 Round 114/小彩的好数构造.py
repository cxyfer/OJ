"""
F-小彩的好数构造
https://ac.nowcoder.com/acm/contest/119273/F

神秘構造題
思路是不要發生進位，故選擇最小的 b = 100...001
接著考慮 a 的構造，需要滿足 a1 + an <= 3 且 a1 + an != a2 且 a1 + an != a{n-1}
分奇偶討論：
- 奇數：a = 131313....1
- 偶數：a = 121212....12
"""

def solve():
    n = int(input())

    if n == 1:
        print(-1)
        return
    if n & 1:
        a = "13" * (n // 2) + '1'
    else:
        a = "12" * (n // 2)
    b = '1' + '0' * (n - 2) + '1'
    print(a, b)

if __name__ == "__main__":
    solve()