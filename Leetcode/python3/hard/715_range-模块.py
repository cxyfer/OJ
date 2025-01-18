#
# @lc app=leetcode.cn id=715 lang=python3
#
# [715] Range 模块
#

# @lc code=start

"""
    Segment Tree
    [线段树详解「汇总级别整理 🔥🔥🔥」](https://leetcode.cn/problems/range-module/solutions/1612955/by-lfool-eo50/)
    模板：https://leetcode.cn/problems/range-module/solutions/1612783/by-himymben-vo9g/
"""
MAX_RANGE = int(1e9 + 7)
class RangeModule:

    def __init__(self):
        self.st = SegmentTree()

    def addRange(self, left: int, right: int) -> None:
        SegmentTree.update(self.st.root, 1, MAX_RANGE, left, right - 1, True)

    def queryRange(self, left: int, right: int) -> bool:
        return SegmentTree.query(self.st.root, 1, MAX_RANGE, left, right - 1)

    def removeRange(self, left: int, right: int) -> None:
        SegmentTree.update(self.st.root, 1, MAX_RANGE, left, right - 1, False)


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)

class Node:
    def __init__(self) -> None:
        self.ls = self.rs = None # Left and Right Son
        self.val = False # 當前節點值
        self.add = False # 懶惰標記

class SegmentTree:
    def __init__(self):
        self.root = Node()
    
    @staticmethod
    def update(node: Node, lc: int, rc: int, l: int, r: int, v: bool) -> None:
        if l <= lc and rc <= r:
            node.val = v
            # 注意產生變化懶標記就為True，因為更新有刪除
            node.add = True
            return
        SegmentTree.pushdown(node)
        mid = (lc + rc) >> 1
        if l <= mid:
            SegmentTree.update(node.ls, lc, mid, l, r, v)
        if r > mid:
            SegmentTree.update(node.rs, mid + 1, rc, l, r, v)
        SegmentTree.pushup(node)
 
    @staticmethod
    def query(node: Node, lc: int, rc: int, l: int, r: int) -> bool:
        if l <= lc and rc <= r:
            return node.val
        # 先確保所有關聯的懶標記下沈下去
        SegmentTree.pushdown(node)
        mid, ans = (lc + rc) >> 1, True
        if l <= mid:
            ans = ans and SegmentTree.query(node.ls, lc, mid, l, r)
        if r > mid:
            # 同樣為不同題目中的更新方式
            ans = ans and SegmentTree.query(node.rs, mid + 1, rc, l, r)
        return ans
    
    @staticmethod
    def pushdown(node: Node) -> None:
        # 懶標記, 在需要的時候才開拓節點和賦值
        if node.ls is None:
            node.ls = Node()
        if node.rs is None:
            node.rs = Node()
        if not node.add:
            return
        node.ls.val = node.val
        node.rs.val = node.val
        # 註意產生變化懶標記就為True，因為更新有刪除
        node.ls.add, node.rs.add = True, True
        node.add = False
    
    @staticmethod
    def pushup(node: Node) -> None:
        # 更新方式：此處為兩者都true
        node.val = node.ls.val and node.rs.val

# @lc code=end

