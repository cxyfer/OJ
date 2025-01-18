"""
    首先做前綴和 s ，如此便可以把區間和轉換為兩個前綴的差。
    之後，對於每個固定的右端點 right ，我們想要找到滿足 s[right] - s[left] = x 的左端點數量。
    這可以通過維護一個哈希表來實現，記錄每個前綴和的出現次數。
"""
from collections import defaultdict

n, x = map(int, input().split())
A = list(map(int, input().split()))

ans = s = 0
cnt = defaultdict(int)
cnt[0] = 1
for i in range(n):
    s += A[i]
    ans += cnt[s - x]
    cnt[s] += 1
print(ans)