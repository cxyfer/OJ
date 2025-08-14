"""
首先思考如何到達 (i, j)，
由 A[i] ^ B[j] = 0 可知需要滿足 A[i] = B[j]，此時考慮前一步 (i - 1, j) 或 (i, j - 1)
也就是需滿足 A[i] = A[i - 1] = B[j] 或 A[i] = B[j] = B[j - 1]，
故若要到達 (i, j)，則需要滿足 A[1..i] 和 B[1..j] 的值皆相同。

為使 A[1..i] 和 B[1..j] 的值皆相同，可以將較少的那一個數字全部變成另一個數字，
故 f(i, j) = min(cnt0(i, j), cnt1(i, j))，其中 cnt0(i, j) 表示 A[1..i] 和 B[1..j] 中 0 的個數，cnt1 同理。

由 min(x, y) = ((x + y) - abs(x - y)) // 2 ，
可改寫成 f(i, j) = (cnt0(i, j) + cnt1(i, j)) // 2 - abs(cnt0(i, j) - cnt1(i, j)) // 2

所求為 sum_{i=1..n} sum_{j=1..n} f(i, j)

考慮第一項，由於 cnt0(i, j) + cnt1(i, j) = i + j，可以計算出第一項為：
    sum_{i=1..n} sum_{j=1..n} (i + j) // 2
 = sum_{i=1..n} sum_{j=1..n} i // 2 + sum_{i=1..n} sum_{j=1..n} j // 2
 = sum_{i=1..n} i * n // 2 + sum_{j=1..n} j * n // 2
 = (n // 2 * (n * (n + 1) // 2) + (n // 2 * (n * (n + 1) // 2)
 = n * n * (n + 1) // 2

考慮第二項，將 cnt0(i, j) - cnt1(i, j) 改寫成：
    cnt0(i, j) - cnt1(i, j)
 = (cnt0(i, 0) + cnt0(0, j)) - (cnt1(i, 0) + cnt1(0, j))
 = (cnt0(i, 0) - cnt1(i, 0)) - (cnt1(0, j) - cnt0(0, j))

可以預處理出 diffa[i] = cnt0(i, 0) - cnt1(i, 0) 和 diffb[j] = cnt1(0, j) - cnt0(0, j)
故第二項可以寫成 sum_{i=1..n} sum_{j=1..n} abs(diffa[i] - diffb[j]) / 2

而 sum_{i=1..n} sum_{j=1..n} abs(diffa[i] - diffb[j])
可以用排序 + 前綴和 + 二分搜尋來在 O(n log n) 的時間內計算。
"""
from bisect import bisect_right
from itertools import accumulate

t = int(input())

def solve():
    n = int(input())
    A = input().strip()
    B = input().strip()

    # diffa[i] = 在 a[0..i] 中 0 的個數減去 1 的個數
    diffa = [0] * n
    cnt = 0
    for i, ch in enumerate(A):
        cnt += (ch == '0')
        diffa[i] = cnt - (i + 1 - cnt)

    # diffb[j] = 在 b[0..j] 中 1 的個數減去 0 的個數
    diffb = [0] * n
    cnt = 0
    for i, ch in enumerate(B):
        cnt += (ch == '1')
        diffb[i] = cnt - (i + 1 - cnt)

    diffa.sort()
    diffb.sort()
    # 預處理 diffb 的 prefix sum
    ps = list(accumulate(diffb, initial=0))
    diff_sum = 0
    for x in diffa:
        # 找到在 diffb 中 <= x 的元素個數 k
        k = bisect_right(diffb, x)
        diff_sum += k * x - ps[k]
        diff_sum += (ps[n] - ps[k]) - (n - k) * x

    ans = n * n * (n + 1) // 2 - diff_sum // 2
    print(ans)

for _ in range(t):
    solve()