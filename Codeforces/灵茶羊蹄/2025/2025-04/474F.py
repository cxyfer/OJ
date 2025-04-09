import math
from bisect import *
from collections import *

import sys
input = sys.stdin.readline
def print(text=""): sys.stdout.write(text + "\n")

class SegmentTree:
    def __init__(self, nums):
        n = len(nums)
        self.nums = [0] + nums # 讓 index 從 1 開始
        self.tree = [0 for _ in range(1 << (n.bit_length() + 1))]
        self.build(1, 1, n)
 
    def build(self, o, left, right): # node, left, right
        if left == right: # Leaf node initialization
            self.tree[o] = self.nums[left]
            return
        mid = (left + right) // 2
        self.build(2*o, left, mid) # left child
        self.build(2*o+1, mid + 1, right) # right child
        self.tree[o] = self.merge(2*o, 2*o+1)
 
    def merge(self, left_child, right_child):
        return math.gcd(self.tree[left_child], self.tree[right_child])
 
    def update(self, o, left, right, idx, val):
        if left == right:
            self.tree[o] = val
            return
        mid = (left + right) // 2
        if idx <= mid:
            self.update(2*o, left, mid, idx, val)
        else:
            self.update(2*o+1, mid + 1, right, idx, val)
        self.tree[o] = self.merge(2*o, 2*o+1)
 
    def query(self, o, left, right, l, r):
        if l <= left and right <= r:
            return self.tree[o]
        mid = (left + right) // 2
        ans = 0
        if l <= mid:
            ans = math.gcd(ans, self.query(2*o, left, mid, l, r))
        if r > mid:
            ans = math.gcd(ans, self.query(2*o+1, mid + 1, right, l, r))
        return ans

n = int(input())
A = list(map(int, input().split()))
q = int(input())

pos = defaultdict(list)
for i, x in enumerate(A, start=1):
    pos[x].append(i)

st = SegmentTree(A)
outs = []
for _ in range(q):
    l, r = map(int, input().split())
    g = st.query(1, 1, n, l, r)
    idx1 = bisect_left(pos[g], l)
    idx2 = bisect_right(pos[g], r)
    outs.append((r - l + 1) - (idx2 - idx1))
print('\n'.join(map(str, outs)))