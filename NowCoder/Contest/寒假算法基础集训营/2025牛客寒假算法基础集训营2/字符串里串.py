from collections import defaultdict

n = int(input())
s = input()

lpos = defaultdict(lambda: n)
rpos = defaultdict(lambda: -1)
for i, ch in enumerate(s):
    lpos[ch] = min(lpos[ch], i)
    rpos[ch] = max(rpos[ch], i)

pre = [0] * n
pre[0] = lpos[s[0]] - 0
for i in range(1, n):
    pre[i] = min(pre[i - 1], lpos[s[i]] - i)
suf = [0] * n
suf[n-1] = rpos[s[n-1]] - (n-1)
for i in range(n-2, -1, -1):
    suf[i] = max(suf[i+1], rpos[s[i]] - i)

def check(k):
    if k <= 1:
        return False
    return (suf[k-1] >= 1) or (pre[n-k] <= -1)

left, right = 1, n
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        left = mid + 1
    else:
        right = mid - 1

print(0 if right < 2 else right)