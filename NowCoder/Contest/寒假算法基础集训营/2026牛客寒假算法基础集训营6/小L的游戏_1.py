"""
K. 小L的游戏
https://ac.nowcoder.com/acm/contest/120566/K
簽到

雙方各操作一次會消耗 (m + n) 個單位，因此根據 z 除以 (m + n) 的餘數，便可以判斷最後是哪一方操作。
"""
def solve():
    m, n, z = map(int, input().split())

    r = z % (m + n)
    if r == 0 or r > m:  # 最後一次是後手操作
        print(1, end='')
    else:  # 最後一次是先手操作
        print(0, end='')

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()