#
# @lc app=leetcode id=3515 lang=python3
#
# [3515] Shortest Path in a Weighted Tree
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class SegNode:
    def __init__(self) -> None:
        self.ls = self.rs = None  # left and right child
        self.val = self.lazy = 0  # value, lazy tag

class SegmentTree:
    def __init__(self, nums: List[int] = None):
        self.nums = nums
        self.root = SegNode()
        if nums is not None and len(nums) > 0:
            self.build(self.root, 1, len(nums))

    def build(self, node: SegNode, left: int, right: int) -> None:
        if left == right:
            node.val = self.nums[left - 1]
            return
        mid = (left + right) // 2
        node.ls = SegNode()
        node.rs = SegNode()
        self.build(node.ls, left, mid)
        self.build(node.rs, mid + 1, right)
        self.pushup(node)  # push up node value

    # update the range [l, r] with value v
    @staticmethod
    def update(node: SegNode, left: int, right: int, l: int, r: int, v: int) -> None:
        if l <= left and right <= r:
            # update node value (Customized)
            SegmentTree._update(node, left, right, v)
            return
        SegmentTree.pushdown(node, left, right) # push down lazy tags
        mid = (left + right) // 2
        if l <= mid:
            SegmentTree.update(node.ls, left, mid, l, r, v)
        if r > mid:
            SegmentTree.update(node.rs, mid + 1, right, l, r, v)
        SegmentTree.pushup(node) # push up node value

    # update node value (Customized)
    @staticmethod
    def _update(node: SegNode, left: int, right: int, v: int) -> None:
        node.val += v * (right - left + 1)
        node.lazy += v

    # query the range [l, r]
    @staticmethod
    def query(node: SegNode, left: int, right: int, l: int, r: int) -> int:
        if l <= left and right <= r:
            return node.val
        # Ensure all lazy tags have been pushed down
        SegmentTree.pushdown(node, left, right) 
        mid = (left + right) // 2
        # Calculate answer (Customized)
        ans = 0
        if l <= mid:
            ans += SegmentTree.query(node.ls, left, mid, l, r)
        if r > mid:
            ans += SegmentTree.query(node.rs, mid + 1, right, l, r)
        return ans
    
    # push down lazy tags
    @staticmethod
    def pushdown(node: SegNode, left: int, right: int) -> None:
        if node.ls is None:
            node.ls = SegNode()
        if node.rs is None:
            node.rs = SegNode()
        if node.lazy != 0:
            # Update node value (Customized)
            mid = (left + right) // 2
            SegmentTree._update(node.ls, left, mid, node.lazy)
            SegmentTree._update(node.rs, mid + 1, right, node.lazy)
            node.lazy = 0
    
    # push up node value
    @staticmethod
    def pushup(node: SegNode) -> None:
        # Update method (Customized)
        node.val = node.ls.val + node.rs.val

class Solution:
    def treeQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        mp = {}
        for u, v, w in edges:
            if u > v:
                u, v = v, u
            g[u].append((v, w))
            g[v].append((u, w))
            mp[(u, v)] = w

        dist = [0] * (n + 1)
        dfns = [0] * (n + 1)
        dfne = [0] * (n + 1)
        time = 0  # timestamp, 1-indexed

        def dfs(u, fa, d):
            nonlocal time
            time += 1
            dfns[u] = time
            dist[u] = d
            for v, w in g[u]:
                if v == fa:
                    continue
                dfs(v, u, d + w)
            dfne[u] = time

        dfs(1, 0, 0)
        st = SegmentTree([0] * n)  # 維護變化量

        ans = []
        for query in queries:
            op, *args = query
            if op == 1:
                u, v, w = args
                if u > v:
                    u, v = v, u
                c = u if dist[u] > dist[v] else v  # 判斷哪個是子節點
                st.update(st.root, 1, n, dfns[c], dfne[c], w - mp[(u, v)])
                mp[(u, v)] = w
            elif op == 2:
                x = args[0]
                ans.append(dist[x] + st.query(st.root, 1, n, dfns[x] , dfns[x]))
        return ans
# @lc code=end

