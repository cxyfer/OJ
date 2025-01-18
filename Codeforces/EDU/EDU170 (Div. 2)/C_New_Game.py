import random

class Wrapper:
    BASE = random.randint(1, 1e9)
    
    def __init__(self, value):
        self.value = value
    
    def __hash__(self):
        return hash(self.value ^ self.BASE)
    
    def __eq__(self, other):
        return isinstance(other, Wrapper) and self.value == other.value

from collections import defaultdict

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    cnt = defaultdict(int)
    for x in A:
        cnt[Wrapper(x)] += 1

    keys = sorted(cnt.keys(), key=lambda x: x.value)
    m = len(keys)
    ans = 0
    cur = 0 # 當前手牌數量
    l = 0 # 左指針
    for r, key in enumerate(keys):
        cur += cnt[key]
        while l <= r and (key.value - keys[l].value > r - l or (r - l + 1) > k):
            cur -= cnt[keys[l]]
            l += 1
        if keys[r].value - keys[l].value == r - l and (r - l + 1) <= k:
            ans = max(ans, cur)
    print(ans)
