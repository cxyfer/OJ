#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    cnt = [0] * k
    for x in s:
        cnt[x % k] += 1
    ans = min(cnt[0], 1)
    for i in range(1, (k + 1) // 2):
        ans += max(cnt[i], cnt[k - i])
    if k % 2 == 0 and cnt[k // 2]:
        ans += 1
    return ans