"""
I. 小L的构造2
https://ac.nowcoder.com/acm/contest/120566/I

構造
原題: https://codeforces.com/contest/2171/problem/E

在做題時就感覺在哪裡做過，然而因為原題允許六組衝突所以可以隨便搞過，
但實際上在 n >= 6 時是必然可以構造出本題要求的答案的。

原題的一種思路是將每 3 個數分成一組，使用 x, y1, y2 的方式來構造，其中 y1 和 y2 有共同的公因數。
那麼依據 SPF 分組，同一組的數中兩兩作為 y，令 f(p) 表示 SPF 為 p 的數的數量，則：
- f(2) = n/2
- f(3) = n/3-n/6 = n/6
- f(5) = n/5-n/10-n/15+n/30 = n/15
由於允許6次衝突，我們可以取前七個質數 2, 3, 5, 7, 11, 13, 17 來構造
由於 f(2) // 2 + f(3) // 2 + f(5) // 2 + ... + f(17) // 2 >= n // 3 ，故必然可以構造出答案。

但是，本題要求沒有衝突，但之前的衝突發生在換組時，故考慮能不能讓先前的換組操作抵消掉。
我們可以用 6 來串接 2 和 3 的兩組，也就是僅使用一組數字作為 y。
由於 2 或 3 的倍數有 1 - (1/2 * 2/3) = 2/3 個，因此可以構造出 n // 3 組。
唯一的例外是當 n < 6 時，此時沒辦法連接 2 和 3 的兩組，因此需要特殊處理，此時只有 n = 4 時有解，且已經在題目中給出。
"""

from math import gcd


def solve():
    n = int(input())

    if n < 6:
        print(3, 4, 2, 1) if n == 4 else print(-1)
        return

    # 分組
    g2, g3, g6, rem = [], [], [], []
    for x in range(1, n + 1):
        if x % 6 == 0:
            g6.append(x)
        elif x % 2 == 0:
            g2.append(x)
        elif x % 3 == 0:
            g3.append(x)
        else:
            rem.append(x)

    # 用 6 串接 2 和 3 的兩組
    arr = g2 + g6 + g3
    m = len(arr)

    # 以 x y y 的方式構造每三個數字'
    ans = [-1] * n
    idx = 1
    j = 0
    while j + 1 < m:
        if idx + 1 < n:
            ans[idx] = arr[j]
            ans[idx + 1] = arr[j + 1]
            idx += 3
        else:
            break
        j += 2
    rem.extend(arr[j:])  # 若有剩餘的數字，則作為額外的 x 使用

    idx = 0
    for x in rem:
        while ans[idx] != -1:
            idx += 1
        ans[idx] = x

    def check():
        for i in range(n - 2):
            if gcd(ans[i], ans[i + 1]) > 1 or gcd(ans[i + 1], ans[i + 2]) > 1 or gcd(ans[i], ans[i + 2]) > 1:
                continue
            return False
        return True

    # assert check()
    print(*ans)


if __name__ == "__main__":
    solve()
