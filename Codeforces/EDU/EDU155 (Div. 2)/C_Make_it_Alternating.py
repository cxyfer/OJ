from math import *

MOD = 998244353
t = int(input())

for tc in range(t):
    s = input()
    s += "!"
    # 算連續0或連續1的個數
    n = len(s)
    ans1 = 0
    ans2 = 1
    pre = s[0]
    cnt = 1 # 連續0或連續1的個數
    for i in range(1, n):
        if s[i] == pre:
            cnt += 1
            ans1 += 1
        else:
            ans2 *= cnt % MOD # C(cnt, cnt-1) = cnt
            pre = s[i]
            cnt = 1
    print(ans1, ans2 * factorial(ans1) % MOD)

