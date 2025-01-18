#
# @lc app=leetcode id=3382 lang=python3
# @lcpr version=30204
#
# [3382] Maximum Area Rectangle With Point Constraints II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class SegNode:
    def __init__(self) -> None:
        self.ls = self.rs = None # left and right child
        self.val = 0

class SegmentTree:
    def __init__(self, n: int):
        self.n = n
        self.root = SegNode()

    # v++
    def update(self, node: SegNode, left: int, right: int, v: int) -> None:
        if left == right:
            node.val += 1
            return
        mid = (left + right) // 2
        if v <= mid:
            if node.ls is None:
                node.ls = SegNode()
            self.update(node.ls, left, mid, v)
        else:
            if node.rs is None:
                node.rs = SegNode()
            self.update(node.rs, mid + 1, right, v)
        self.pushup(node) # push up node value
 
    # query the range [l, r]
    def query(self, node: SegNode, left: int, right: int, l: int, r: int) -> int:
        if node is None:
            return 0
        if l <= left and right <= r:
            return node.val
        mid = (left + right) // 2
        ans = 0
        if l <= mid:
            ans += self.query(node.ls, left, mid, l, r)
        if r > mid:
            ans += self.query(node.rs, mid + 1, right, l, r)
        return ans
    
    # push up node value
    def pushup(self, node: SegNode) -> None:
        node.val = (0 if node.ls is None else node.ls.val) + (0 if node.rs is None else node.rs.val)

class Solution:
    def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
        points = list(zip(xCoord, yCoord))

        # 依照 x 座標排序
        points.sort(key=lambda p: p[0])

        xMap = defaultdict(list)
        for x, y in points:
            xMap[x].append(y)

        # 離散化 y 座標
        ySorted = sorted(set([p[1] for p in points]))
        yMap = {y : i for i, y in enumerate(ySorted, 1)}

        seg = SegmentTree(len(ySorted))

        ans = -1
        Xs = sorted(xMap.keys())
        last = defaultdict(lambda: (0, float('inf'))) # (cnt, x)
        for x2 in Xs: # 枚舉右邊界
            Ys = xMap[x2]
            Ys.sort()
            for y in Ys:
                seg.update(seg.root, 1, seg.n, yMap[y])
            for y1, y2 in pairwise(Ys): # 枚舉右上和右下
                yy1, yy2 = yMap[y1], yMap[y2]
                cnt2 = seg.query(seg.root, 1, seg.n, yy1, yy2)
                cnt1, x1 = last[(yy1, yy2)]
                if cnt2 - cnt1 == 2:
                    ans = max(ans, (x2 - x1) * (y2 - y1))
                last[(yy1, yy2)] = (cnt2, x2)
        return ans
# @lc code=end

sol = Solution()
print(sol.maxRectangleArea([1,1,3,3],[1,3,1,3])) # 4
print(sol.maxRectangleArea([1,1,3,3,2],[1,3,1,3,2])) # -1
print(sol.maxRectangleArea([1,1,3,3,1,3],[1,3,1,3,2,2])) # 2
print(sol.maxRectangleArea([89,55,89,55,0,34,17,71,98,90,63,49,76,72,4,46,67,94,52,6],[58,69,69,58,100,36,14,40,13,41,29,23,47,52,95,49,37,77,54,59])) # 374

#
# @lcpr case=start
# [1,1,3,3]\n[1,3,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,3,3,2]\n[1,3,1,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,3,3,1,3]\n[1,3,1,3,2,2]\n
# @lcpr case=end

#

