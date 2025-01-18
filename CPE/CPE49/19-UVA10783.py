""" UVA-10783: Odd Sum
    # brute force / prefix sum
"""
from itertools import accumulate

T = int(input())
pre_sum = list(accumulate([i if i & 1 else 0 for i in range(101)], initial=0))

for tc in range(1, T+1):
    try:
        a = int(input())
        b = int(input())
    except EOFError:
        break
    print(f"Case {tc}: {pre_sum[b+1] - pre_sum[a]}")