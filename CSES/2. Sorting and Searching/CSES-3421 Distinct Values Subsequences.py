"""
固定右端點 nums[i] ，則可以在 [0, i) 中選擇任意個與 nums[i] 不同，且互不重複的數字。
若一個數字 nums[j] 出現了 k 次，則可以從這 k 個數字中選擇一個、或不選擇，總共有 k + 1 種選擇。
"""
from collections import defaultdict

MOD = int(1e9 + 7)
n = int(input())
A = list(map(int, input().split()))

ans = left = 0
cur = 1
cnt = defaultdict(int)
for right, x in enumerate(A):
    # 先排除 nums[i] 的影響
    # cur //= (cnt[x] + 1)
    cur = cur * pow(cnt[x] + 1, MOD - 2, MOD) % MOD

    cnt[x] += 1
    ans = (ans + cur) % MOD

    # 重新考慮 nums[i] 的影響
    # cur *= (cnt[x] + 1)
    cur = cur * (cnt[x] + 1) % MOD
print(ans % MOD)