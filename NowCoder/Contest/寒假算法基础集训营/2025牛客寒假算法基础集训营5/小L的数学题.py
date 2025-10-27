"""
I - 小L的数学题
https://ac.nowcoder.com/acm/contest/95337/I

證明很麻煩，但可以打表猜出如下結論：
- 當 n > 0 時，可以產生 > 0 的所有數字
- 當 n = 0 時，只能產生 0
"""

def solve():
    n, m = map(int, input().split())

    if n > 0 and m > 0 or n == 0 and m == 0:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()