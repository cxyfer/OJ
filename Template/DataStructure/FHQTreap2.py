"""
FHQ Treap 模板
使用 pool 管理節點，避免重複分配和釋放記憶體
"""

from __future__ import annotations
from random import getrandbits

# fmt: off
import sys
it = iter(sys.stdin.read().splitlines())
def input():
    return next(it)
def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)) + end)
# fmt: on


class FHQTreap:
    __slots__ = ("left", "right", "sz", "pri", "val", "lazy", "idx")

    def __init__(self, max_nodes: int = 200_000) -> None:
        self.left = [0] * (max_nodes + 1)
        self.right = [0] * (max_nodes + 1)
        self.sz = [0] * (max_nodes + 1)
        self.pri = [0] * (max_nodes + 1)
        self.val = [0] * (max_nodes + 1)
        self.lazy = [0] * (max_nodes + 1)
        self.idx = 0

    def _expand(self) -> None:
        extend_size = max(1, len(self.val) - 1)
        self.left.extend([0] * extend_size)
        self.right.extend([0] * extend_size)
        self.sz.extend([0] * extend_size)
        self.pri.extend([0] * extend_size)
        self.val.extend([0] * extend_size)
        self.lazy.extend([0] * extend_size)

    def size(self, root: int) -> int:
        return self.sz[root] if root else 0

    def make(self, value: int) -> int:
        self.idx += 1
        if self.idx >= len(self.val):
            self._expand()

        self.left[self.idx] = 0
        self.right[self.idx] = 0
        self.sz[self.idx] = 1
        self.pri[self.idx] = getrandbits(32)
        self.val[self.idx] = value
        self.lazy[self.idx] = 0
        return self.idx

    def pushup(self, root: int) -> None:
        if root == 0:
            return
        self.sz[root] = self.sz[self.left[root]] + self.sz[self.right[root]] + 1

    def apply(self, o: int, value: int) -> None:
        if o == 0:
            return
        self.val[o] += value
        self.lazy[o] += value

    def pushdown(self, root: int) -> None:
        if root == 0 or self.lazy[root] == 0:
            return
        tag = self.lazy[root]
        self.apply(self.left[root], tag)
        self.apply(self.right[root], tag)
        self.lazy[root] = 0

    def split(self, root: int, key: int) -> tuple[int, int]:
        """Split into values < key and values >= key."""
        if root == 0:
            return 0, 0

        self.pushdown(root)
        if self.val[root] < key:
            a, b = self.split(self.right[root], key)
            self.right[root] = a
            self.pushup(root)
            return root, b

        a, b = self.split(self.left[root], key)
        self.left[root] = b
        self.pushup(root)
        return a, root

    def merge(self, a: int, b: int) -> int:
        """Merge two trees where every value in a is <= every value in b."""
        if a == 0 or b == 0:
            return a if a else b

        if self.pri[a] < self.pri[b]:
            self.pushdown(a)
            self.right[a] = self.merge(self.right[a], b)
            self.pushup(a)
            return a
        else:
            self.pushdown(b)
            self.left[b] = self.merge(a, self.left[b])
            self.pushup(b)
            return b

    def add(self, root: int, value: int) -> int:
        """Insert one value. Duplicates are allowed."""
        a, b = self.split(root, value)
        mid = self.make(value)
        return self.merge(self.merge(a, mid), b)

    def remove(self, root: int, value: int) -> int:
        """Erase one occurrence of value if it exists."""
        if root == 0:
            return 0
        self.pushdown(root)
        if self.val[root] == value:
            return self.merge(self.left[root], self.right[root])
        if value < self.val[root]:
            self.left[root] = self.remove(self.left[root], value)
        else:
            self.right[root] = self.remove(self.right[root], value)
        self.pushup(root)
        return root

    def update(self, root: int, left: int, right: int, value: int) -> int:
        """Add value to all keys in [left, right)."""
        a, b = self.split(root, left)
        c, d = self.split(b, right)
        self.apply(c, value)
        return self.merge(self.merge(a, c), d)

    def popmin(self, root: int) -> int:
        """Remove the minimum value from the tree."""
        if root == 0:
            return 0
        self.pushdown(root)
        if self.left[root] == 0:
            return self.right[root]
        self.left[root] = self.popmin(self.left[root])
        self.pushup(root)
        return root

    def popmax(self, root: int) -> int:
        """Remove the maximum value from the tree."""
        if root == 0:
            return 0
        self.pushdown(root)
        if self.right[root] == 0:
            return self.left[root]
        self.right[root] = self.popmax(self.right[root])
        self.pushup(root)
        return root

    def front(self, root: int) -> int:
        """Return the minimum value. Requires root is not 0."""
        if root == 0:
            raise IndexError("front from empty FHQTreap")
        self.pushdown(root)
        while self.left[root]:
            root = self.left[root]
            self.pushdown(root)
        return self.val[root]

    def back(self, root: int) -> int:
        """Return the maximum value. Requires root is not 0."""
        if root == 0:
            raise IndexError("back from empty FHQTreap")
        self.pushdown(root)
        while self.right[root]:
            root = self.right[root]
            self.pushdown(root)
        return self.val[root]

    def bisect_left(self, root: int, key: int) -> int:
        """Return how many values are < key."""
        if root == 0:
            return 0
        self.pushdown(root)
        if self.val[root] < key:
            return self.size(self.left[root]) + 1 + self.bisect_left(self.right[root], key)
        else:
            return self.bisect_left(self.left[root], key)

    def bisect_right(self, root: int, key: int) -> int:
        """Return how many values are <= key."""
        if root == 0:
            return 0
        self.pushdown(root)
        if self.val[root] <= key:
            return self.size(self.left[root]) + 1 + self.bisect_right(self.right[root], key)
        else:
            return self.bisect_right(self.left[root], key)

    def kth(self, root: int, k: int) -> int:
        """Return the 0-indexed kth value."""
        if root == 0 or k < 0 or k >= self.size(root):
            raise IndexError("FHQTreap index out of range")
        self.pushdown(root)
        left_size = self.size(self.left[root])
        if k < left_size:
            return self.kth(self.left[root], k)
        elif k == left_size:
            return self.val[root]
        else:
            return self.kth(self.right[root], k - left_size - 1)

    def predecessor(self, root: int, key: int) -> int:
        """Return the largest value < key. Requires the answer to exist."""
        return self.kth(root, self.bisect_left(root, key) - 1)

    def successor(self, root: int, key: int) -> int:
        """Return the smallest value > key. Requires the answer to exist."""
        return self.kth(root, self.bisect_right(root, key))


# P3369 【模板】普通平衡树
def P3369():
    n = int(input())

    tr = FHQTreap(n + 5)
    root = 0

    ans = []
    for _ in range(n):
        op, x = map(int, input().split())
        if op == 1:
            root = tr.add(root, x)
        elif op == 2:
            root = tr.remove(root, x)
        elif op == 3:
            ans.append(tr.bisect_left(root, x) + 1)
        elif op == 4:
            ans.append(tr.kth(root, x - 1))
        elif op == 5:
            ans.append(tr.predecessor(root, x))
        elif op == 6:
            ans.append(tr.successor(root, x))

    print(*ans, sep="\n")

P3369()