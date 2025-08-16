from typing import List

"""
Lazy Segment Tree
- 動態開點，只有當需要用到子節點時，才會創建子節點
- 使用 SegInfo 來維護要維護的資訊，好處是直接可以使用 + 運算符來合併兩個 SegInfo，缺點是會有重新創建 SegInfo 物件的效能損失
- 基本上只需要 SegInfo 的合併方法，以及 apply 方法即可，若遇到效能問題，可以考慮把需要重新創建 SegInfo 物件的部分改為直接賦值

Problem:
- 731. My Calendar II
- 732. My Calendar III
- P3372 【模板】线段树 1
"""

class SegInfo:
    def __init__(self, s: int = 0) -> None:
        self.s = s

    # 使用 + 運算符來合併兩個 SegInfo，但要注意效能問題
    def __add__(self, other: 'SegInfo') -> 'SegInfo':
        return SegInfo(self.s + other.s)

    def __iadd__(self, other: 'SegInfo') -> 'SegInfo':  # self += other
        self.s += other.s
        return self


class SegNode:
    def __init__(self) -> None:
        self.ls = self.rs = None  # left and right child
        self.val = SegInfo()  # value
        self.lazy = 0  # lazy tag


class SegmentTree:
    def __init__(self, nums: List[int] = None):
        self.n = len(nums)
        self.root = SegNode()
        if nums is not None and len(nums) > 0:
            self.build(self.root, 1, self.n, nums)

    def update(self, l: int, r: int, v: int) -> None:
        self._update(self.root, 1, self.n, l, r, v)

    def query(self, l: int, r: int) -> SegInfo:
        return self._query(self.root, 1, self.n, l, r)

    def build(self, node: SegNode, left: int, right: int, nums: List[int]) -> None:
        if left == right:
            node.val = SegInfo(nums[left - 1])
            # 若使用 SegInfo(nums[left - 1]) 超時，考慮直接賦值
            # node.val.s = nums[left - 1]
            return
        mid = (left + right) // 2
        node.ls = SegNode()
        node.rs = SegNode()
        self.build(node.ls, left, mid, nums)
        self.build(node.rs, mid + 1, right, nums)
        self.pushup(node)  # push up node value

    # update the range [l, r] with value v
    def _update(self, node: SegNode, left: int, right: int, l: int, r: int, v: int) -> None:
        if l <= left and right <= r:
            # apply lazy tag
            self.apply(node, left, right, v)
            return
        self.pushdown(node, left, right)  # push down lazy tags
        mid = (left + right) // 2
        if l <= mid:
            self._update(node.ls, left, mid, l, r, v)
        if r > mid:
            self._update(node.rs, mid + 1, right, l, r, v)
        self.pushup(node)  # push up node value

    # apply lazy tag
    def apply(self, node: SegNode, left: int, right: int, v: int) -> None:
        node.val.s += v * (right - left + 1)
        node.lazy += v

    # query the range [l, r]
    def _query(self, node: SegNode, left: int, right: int, l: int, r: int) -> SegInfo:
        if l <= left and right <= r:
            return node.val
        # Ensure all lazy tags have been pushed down
        self.pushdown(node, left, right)
        mid = (left + right) // 2
        # Calculate answer (Customized)
        ans = SegInfo()
        if l <= mid:
            ans += self._query(node.ls, left, mid, l, r)
        if r > mid:
            ans += self._query(node.rs, mid + 1, right, l, r)
        return ans

    # push down lazy tags
    def pushdown(self, node: SegNode, left: int, right: int) -> None:
        if node.ls is None:
            node.ls = SegNode()
        if node.rs is None:
            node.rs = SegNode()
        if node.lazy != 0:
            # apply lazy tag
            mid = (left + right) // 2
            self.apply(node.ls, left, mid, node.lazy)
            self.apply(node.rs, mid + 1, right, node.lazy)
            node.lazy = 0  # reset lazy tag

    # push up node value
    def pushup(self, node: SegNode) -> None:
        # update node value
        node.val = node.ls.val + node.rs.val
        # 若使用 + 超時，考慮直接賦值
        # node.val.s = node.ls.val.s + node.rs.val.s