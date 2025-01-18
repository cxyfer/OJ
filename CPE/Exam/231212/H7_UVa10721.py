from functools import *

"""
    DP
    n 個units, k 個bars, 每個bar最多m個units
    第一個unit必須是black
"""

@cache
def BC(n, k, m):
    if n == 0: # 沒有unit了，若還有bar則不滿足
        return 1 if k == 0 else 0
    if k == 1: # 只有1個bar，若滿足限制條件則有1種可能
        return 1 if n <= m else 0
    res = 0
    for x in range(1, min(n, m)+1):
        res += BC(n-x, k-1, m) # 剩下n-x個units, k-1個bars, 每個bar最多還是m個units
    return res

while True:
    try:
        n, k, m = map(int, input().split())  
    except EOFError:
        break
    print(BC(n, k, m))