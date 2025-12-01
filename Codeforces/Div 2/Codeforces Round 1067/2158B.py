"""
構造 + 貪心 + 數學

首先注意到出現頻率為奇數的數字，必定會對答案產生貢獻；
而出現頻率為偶數的數字，若要對答案產生貢獻，則需要劃分成(奇數+奇數)的形式。

考慮能否滿足最優分配，以及若不滿足時需要如何調整。
令 even 表示出現頻率為偶數的數字個數，odd 表示出現頻率為奇數的數字個數。
其中出現頻率為奇數的數字在左側的數量為 x，在右側的數量為 y。
由於 x + y 必為偶數，故 x 和 y 的奇偶性相同。

由於奇數可以寫成 2k+1 的形式，考慮左側的數量，需要滿足 2k + even + x = n
如果 n - even 是奇數，則需要使 x 為奇數用來調整奇偶性才能保證最優分配。
而 x 只有在 odd = 0 時才不可能為奇數，此時則只能捨去一組偶數來調整奇偶性。
"""
from collections import Counter

def solve():
    n = int(input())
    A = list(map(int, input().split()))

    cnt = [0] * 2
    for _, v in Counter(A).items():
        cnt[v & 1] += 1

    ans = cnt[1] + 2 * cnt[0]
    if (n - cnt[0]) & 1 and cnt[1] == 0:
        ans -= 2
    print(ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()