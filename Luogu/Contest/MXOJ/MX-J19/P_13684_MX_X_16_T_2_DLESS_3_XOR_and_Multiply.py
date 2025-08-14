"""
逐位討論，相同的位元可以設為 1，不同的位元可以設為 1 或 0，但只需考慮不同的最高位即可。

令 a / b 為最高的不同位，b / q 為此位後的低位，則所求為最大化
(c + a + b) * (c + p + q)
= c(c + a + b + p + q) + (a + b)(p + q)
由於不同的位元一定是一個是 0，一個是 1，所以 (a + p) 和 (b + q) 都是定值。

考慮 a / p 中哪一個為 0，可以得到兩種情況：
1. (a + b)q = aq + bq
2. b(p + q) = bp + bq

此時只需考慮 b 和 q 如何取，以情況 1 為例，由於 a > b，所以最大化 q，也就是將 q 設為全 1，可以得到最大值
"""

T = int(input())

for _ in range(T):
    x, y, h = map(int, input().split())

    msk = (1 << h) - 1
    if x == y:
        print(msk * msk)
        continue

    # 找到 x 和 y 從高位算起第一個不同的位 k
    k = (x ^ y).bit_length() - 1

    # hi: k 位以上（不包含第 k 位）的部分，這些位上 x 和 y 相同，a 和 b 皆為 1
    hi = ~((1 << (k + 1)) - 1) & msk

    msk_lo = (1 << k) - 1
    # lo: k 位以下（不包含第 k 位）的部分，當 x 和 y 的位相同時，a 和 b 的對應位都設為 1
    lo = (~(x ^ y)) & msk_lo

    # 1. 讓 a 在第 k 位為 1，並最大化 b 的低位，即將低位全設為 1
    ans1 = (hi | (1 << k) | lo) * (hi | msk_lo)
    # 2. 讓 b 在第 k 位為 1，並最大化 a 的低位，即將低位全設為 1
    ans2 = (hi | msk_lo) * (hi | (1 << k) | lo)

    print(max(ans1, ans2))