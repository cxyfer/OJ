"""
    首先做前綴和 s ，如此便可以把區間和轉換為兩個前綴的差。
    之後，對於每個固定的右端點 right ，我們想要使得 s[right] - s[left] 最大，因此我們可以找到一個最小的 s[left]

    相比於 CSES-1643 ，我們的子陣列大小有限制，
    因此我們需要在 s[left] 已經不在合法範圍時，將其移除，並找到下一個合法且最小的 s[left]
    這可以用一個單調佇列來維護
"""

from heapq import heappush, heappop
from itertools import accumulate

n, a, b = map(int, input().split())
X = list(map(int, input().split()))

s = list(accumulate(X, initial=0))

hp = [] # (s[i], i)
ans = float('-inf')
for i in range(n + 1):
    while hp and hp[0][1] < i - b: # 超過範圍
        heappop(hp)
    if i >= a: # 進入合法範圍
        heappush(hp, (s[i - a], i - a))
    if hp: # 有合法的左端點
        ans = max(ans, s[i] - hp[0][0])
print(ans)