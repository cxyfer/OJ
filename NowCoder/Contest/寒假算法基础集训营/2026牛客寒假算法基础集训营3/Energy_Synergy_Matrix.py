"""
F. Energy Synergy Matrix
https://ac.nowcoder.com/acm/contest/120563/F

若沒有障礙，則需要走 n - 1 步，而當每次被迫改變所在的橫列時，會增加 1 的代價。
而由於添加障礙不能破壞連通性，因此先手(A)可以放置如下的位置，此時後手(B)只有放置在如下的位置才能增加1次代價。

....B
..A..

這個局面每 5 個直行會重複一次，因此答案為 (n - 1) + (n // 5)。
"""
def solve():
    n = int(input())
    print((n - 1) + (n // 5))

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()