"""
E. 小苯的有趣数
https://ac.nowcoder.com/acm/contest/116658/E

注意到操作等於重新分配陣列中的數字，且所有數字都是正整數。
而 1 一定是有趣數字，故答案至少為 n - 1，因此我們只需要檢查答案是否為 n 即可。
換句話說，我們只需要關注是否可以使用 n 個有趣數字湊出 sum(A)，這可以用完全背包來解決。
"""
import math

MAX_N = 100
MAX_X = 100 * 200 + 5
vals = []
for x in range(1, int(math.sqrt(MAX_X + 1))):
    if x * x > MAX_X:
        break
    s = sum(map(int, str(x * x)))
    if int(math.sqrt(s)) * int(math.sqrt(s)) == s:
        vals.append(x * x)

# f[i][j] 表示是否可以用 i 個有趣數字湊出 j
# f = [[False] * (MAX_X + 1) for _ in range(MAX_N + 1)]
f = [0] * (MAX_X + 1)
f[0] = 1
for val in vals:
    for i in range(1, MAX_N + 1):
        f[i] |= f[i - 1] >> val
        # for j in range(val, MAX_X + 1):
        #     if f[i - 1][j - val]:
        #         f[i][j] = True

def solve():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n
    s = sum(A)
    print(n if (f[n] & (1 << s)) else n - 1)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()