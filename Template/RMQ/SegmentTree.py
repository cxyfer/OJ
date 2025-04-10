MAX_RANGE = int(1e9 + 7)

class MyCalendar:

    def __init__(self):
        self.st = SegmentTree()

    def book(self, start: int, end: int) -> bool:
        if SegmentTree.query(self.st.root, 0, MAX_RANGE, start, end - 1) != 0:
            return False
        SegmentTree.update(self.st.root, 0, MAX_RANGE, start, end - 1, 1)
        return True

class Node:
    def __init__(self) -> None:
        self.ls = self.rs = None # Left and Right Son
        self.val = 0 # 當前節點值
        self.add = 0 # 懶惰標記

class SegmentTree:
    def __init__(self):
        self.root = Node()
    
    @staticmethod
    def update(node: Node, st: int, ed: int, l: int, r: int, val: int) -> None:
        if l <= st and ed <= r:
            node.val += val
            node.add += val
            return
        SegmentTree.pushdown(node)
        mid = (st + ed) >> 1
        if l <= mid:
            SegmentTree.update(node.ls, st, mid, l, r, val)
        if r > mid:
            SegmentTree.update(node.rs, mid + 1, ed, l, r, val)
        SegmentTree.pushup(node)
 
    @staticmethod
    def query(node: Node, st: int, ed: int, l: int, r: int) -> bool:
        if l <= st and ed <= r:
            return node.val
        # 先確保所有關聯的懶標記下沈下去
        SegmentTree.pushdown(node)
        mid = (st + ed) >> 1
        ans = 0
        if l <= mid:
            ans = max(ans, SegmentTree.query(node.ls, st, mid, l, r))
        if r > mid:
            ans = max(ans, SegmentTree.query(node.rs, mid + 1, ed, l, r))
        return ans
    
    @staticmethod
    def pushdown(node: Node) -> None:
        # 懶標記, 在需要的時候才開拓節點和賦值
        if node.ls is None:
            node.ls = Node()
        if node.rs is None:
            node.rs = Node()
        if node.add == 0:
            return
        node.ls.val += node.val
        node.rs.val += node.val
        node.ls.add += node.val
        node.rs.add += node.val
        node.add = 0
    
    @staticmethod
    def pushup(node: Node) -> None:
        node.val = max(node.ls.val, node.rs.val)