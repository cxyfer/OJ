"""
Similar:
- 3934. Smallest Unique Subarray
"""

from collections import defaultdict
from random import randint

MOD = 1070777777
BASE = randint(int(1e8), int(1e9))


def solve():
    n, k = map(int, input().split())
    nums = [int(input()) for _ in range(n)]

    P = [1] + [0] * n
    for i in range(n):
        P[i + 1] = P[i] * BASE % MOD

    def check(mid: int) -> bool:
        hs = 0
        cnt = defaultdict(int)
        for right, x in enumerate(nums):
            hs = hs * BASE + x
            hs %= MOD
            if right + 1 >= mid:
                cnt[hs] += 1
                hs -= nums[right + 1 - mid] * P[mid - 1]
                hs %= MOD
        return any(v >= k for v in cnt.values())

    left, right = 0, n
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            left = mid + 1
        else:
            right = mid - 1
    print(right)


if __name__ == "__main__":
    solve()
