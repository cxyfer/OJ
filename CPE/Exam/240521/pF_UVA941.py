"""
    AC: UVA, CPE, ZeroJudge
"""
from math import factorial

t = int(input())

for _ in range(t):
    s = sorted(input()) # 記得排序，坑
    n = int(input())

    ans = ""
    while len(s) > 0:
        x = factorial(len(s)-1)
        i = n // x # 回溯法要逐個確定，但其實可以直接計算
        ans += s[i]
        s = s[:i] + s[i+1:] # 刪除已經用過的字元
        n %= x
    print(ans)

"""


abcde
4! = 24
119 / 24 = 4 ... 23

abcd
3! = 6
23 / 6 = 3 ... 5

"""