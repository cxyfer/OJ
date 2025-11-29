"""
P14576 Lamborghini Remix
https://www.luogu.com.cn/problem/P14576

貪心 + 前綴和 + 滑動窗口

為了能在同一行中放入盡量多的光標，顯然是要將光標移動到長度最大的行中。
任兩個光標之間的距離是不會改變的，因此所求為最多有幾個連續的光標，其距離之和不超過最大行長度。
注意換行也會計入距離，因此兩個光標的距離是該行長度加一。
"""
from itertools import accumulate

def solve():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n

    mx = max(A)
    s = list(accumulate(A, func=lambda x, y: x + y + 1))

    ans = left = 0
    for right, x in enumerate(s):
        while x - s[left] > mx:
            left += 1
        ans = max(ans, right - left + 1)
    print(ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()