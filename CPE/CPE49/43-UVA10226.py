"""
    需要做輸出優化，否則在UVA上會TLE
    UVA 使用的 Python 3.5 不支援 Counter.total()，所以要改成 sum(cnt.values())
"""

import sys
from collections import Counter

input = sys.stdin.readline

T = int(input().strip())
input() # 空行
for tc in range(T):
    cnt = Counter()
    line = input().strip()
    while line != "":
        cnt[line] += 1
        try:
            line = input().strip()
        except EOFError:
            break
    # tol = cnt.total() # Python 3.10 才加入
    tol = sum(cnt.values())
    for k, v in sorted(cnt.items()):
        print(f"{k} {v/tol*100:.4f}")
    if tc < T - 1:
        print()