"""
ARC100C - Or Plus Max
https://atcoder.jp/contests/arc100/tasks/arc100_c
SOS DP 高維前綴和

令 f[s] 表示 <= s 的數字有多少個，可以透過高維前綴和求得。
則對於每個數字 x，滿足條件的數字有 f[999999 - x] 個，注意考慮自配對的情況。
"""
def solve():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n
    D = 6
    U = 10 ** D

    f = [0] * U
    for x in A:
        f[x] += 1

    for d in range(D):
        base = 10 ** d
        for s in range(U):
            if (s // base) % 10 == 0:  # 這一維為 0 時沒有轉移來源
                continue
            f[s] += f[s - base]  # 前綴和，從這一維的前一個數字轉移而來

    ans = 0
    for x in A:
        ans += f[(U - 1) - x]
        ans -= all(int(c) < 5 for c in str(x))  # 自配對的情況
    ans //= 2  # 每對數字都被計算了兩次
    print(ans)

if __name__ == '__main__':
    solve()