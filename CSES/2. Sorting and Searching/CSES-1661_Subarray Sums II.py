"""
    跟 1660 基本上一樣，只是測試資料卡了一個雜湊碰撞
"""
from collections import defaultdict
import random

BASE = random.randint(1, 1e9)
class Wrapper:
    def __init__(self, value):
        self.value = value
    
    def __hash__(self):
        return hash(self.value ^ BASE)
    
    def __eq__(self, other):
        return isinstance(other, Wrapper) and self.value == other.value

n, x = map(int, input().split())
A = list(map(int, input().split()))

ans = s = 0
cnt = defaultdict(int)
cnt[Wrapper(0)] = 1
for i in range(n):
    s += A[i]
    ans += cnt[Wrapper(s - x)]
    cnt[Wrapper(s)] += 1
print(ans)
