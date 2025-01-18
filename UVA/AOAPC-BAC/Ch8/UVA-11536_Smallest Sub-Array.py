"""
    Python TLE
"""

import sys
input = sys.stdin.readline
def print(val=""): sys.stdout.write(str(val) + "\n")

N = int(1e6 + 5)
nums = [0] * N
for i in range(3):
    nums[i] = i + 1

t = int(input())
for kase in range(1, t + 1):
    n, m, k = map(int, input().split())
    for i in range(3, n):
        nums[i] = (nums[i - 1] + nums[i - 2] + nums[i - 3]) % m + 1
    ans, left, have = n + 1, 0, 0
    cnt = [0] * (k + 1)
    for right in range(n):
        x = nums[right]
        if x > k:
            continue
        if cnt[x] == 0:
            have += 1
        cnt[x] += 1
        while have == k:
            ans = min(ans, right - left + 1)
            if nums[left] <= k:
                cnt[nums[left]] -= 1
                if cnt[nums[left]] == 0:
                    have -= 1
            left += 1
    print(f"Case {kase}: {ans if ans != n + 1 else 'sequence nai'}")
