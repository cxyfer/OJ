import sys
input = sys.stdin.readline
def print(val=""): sys.stdout.write(str(val) + "\n")

from typing import List

"""
    用我目前掌握的 Python 模板都會超時 QQ
"""

class SegNode:
    def __init__(self) -> None:
        self.ls = self.rs = None # left and right child
        self.val = self.lazy = 0 # value, lazy tag

class SegmentTree:
    def __init__(self):
        self.root = SegNode()
    
    # update the range [l, r] with value v
    @staticmethod
    def update(node: SegNode, left: int, right: int, l: int, r: int, v: int) -> None:
        if l <= left and right <= r:
            node.lazy += v
            node.val += v
            return
        SegmentTree.pushdown(node) # push down lazy tags
        mid = (left + right) // 2
        if l <= mid:
            SegmentTree.update(node.ls, left, mid, l, r, v)
        if r > mid:
            SegmentTree.update(node.rs, mid + 1, right, l, r, v)
        SegmentTree.pushup(node) # push up node value
 
    # query the range [l, r]
    @staticmethod
    def query(node: SegNode, left: int, right: int, l: int, r: int) -> int:
        if l <= left and right <= r:
            return node.val
        # Ensure all lazy tags have been pushed down
        SegmentTree.pushdown(node) 
        # Calculate answer: sum of the range
        ans = 0
        mid = (left + right) // 2
        if l <= mid:
            ans = SegmentTree.query(node.ls, left, mid, l, r)
        if r > mid:
            ans += SegmentTree.query(node.rs, mid + 1, right, l, r)
        return ans
    
    # push down lazy tags
    @staticmethod
    def pushdown(node: SegNode) -> None:
        if node.ls is None:
            node.ls = SegNode()
        if node.rs is None:
            node.rs = SegNode()
        if node.lazy:
            node.ls.lazy += node.lazy
            node.rs.lazy += node.lazy
            node.ls.val += node.lazy
            node.rs.val += node.lazy
            node.lazy = 0
    
    # push up node value
    @staticmethod
    def pushup(node: SegNode) -> None:
        # Update method: sum of the range
        node.val = node.ls.val + node.rs.val

n, q = map(int, input().split())
arr = list(map(int, input().split()))
st = SegmentTree()

st.update(st.root, 0, n - 1, 0, 0, arr[0])
for i in range(1, n):
    st.update(st.root, 0, n - 1, i, i, arr[i] - arr[i - 1])

for _ in range(q):
    t, *args = map(int, input().split())
    if t == 1:
        a, b, u = args
        st.update(st.root, 0, n - 1, a - 1, a - 1, u)
        if b < n:
            st.update(st.root, 0, n - 1, b, b, -u)
    else:
        k = args[0]
        print(st.query(st.root, 0, n - 1, 0, k - 1))