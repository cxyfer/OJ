import sys
sys.setrecursionlimit(int(1e6))

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
        # Calculate answer: sum of range
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
        # Update method: sum of range
        node.val = node.ls.val + node.rs.val

n = int(input())
nums = list(map(int, input().split()))
queries = list(map(int, input().split()))

st = SegmentTree()

for i, x in enumerate(nums):
    SegmentTree.update(st.root, 0, n - 1, i, i, 1)

for q in queries:
    left, right = 0, n
    while left <= right:
        mid = (left + right) // 2
        # print("check", mid, SegmentTree.query(st.root, 0, n - 1, 0, mid))
        if SegmentTree.query(st.root, 0, n - 1, 0, mid) >= q:
            right = mid - 1
        else:
            left = mid + 1
    print(nums[left], end=" ")
    SegmentTree.update(st.root, 0, n - 1, left, left, -1)
print()
