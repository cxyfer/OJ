"""
    雖然遇到 5^r 會產生 r 個 0，但是從種類的角度來看只會多 1 種。

    若 5^r - 1 有 x 個 0，
    則 5^r, 5^r + 1, 5^r + 2, ..., 5^r + 4 都會比 5^r - 1 多 r 個 0，有 x + r 個 0。
    且區間中不存在 x + 1, x + 2, ..., x + r - 1 個 0。
"""

import sys
input = sys.stdin.readline
def print(val=""): sys.stdout.write(str(val)+"\n")

while True:
    l, r = map(int, input().split())
    if l == r == 0:
        break
    a, b = l // 5, r // 5
    print(b - a + 1)