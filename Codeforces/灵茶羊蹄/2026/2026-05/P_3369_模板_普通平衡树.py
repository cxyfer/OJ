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
    class Node:
        __slots__ = ("left", "right", "sz", "pri", "val", "lazy")

        def __init__(self, val: int, pri: int) -> None:
            self.left: FHQTreap.Node | None = None
            self.right: FHQTreap.Node | None = None
            self.sz = 1
            self.pri = pri
            self.val = val
            self.lazy = 0

    def size(self, root: Node | None) -> int:
        return root.sz if root is not None else 0

    def make(self, value: int) -> Node:
        return self.Node(value, getrandbits(32))

    def pushup(self, root: Node | None) -> None:
        if root is None:
            return
        root.sz = self.size(root.left) + self.size(root.right) + 1

    def apply(self, root: Node | None, value: int) -> None:
        if root is None:
            return
        root.val += value
        root.lazy += value

    def pushdown(self, root: Node | None) -> None:
        if root is None or root.lazy == 0:
            return
        tag = root.lazy
        self.apply(root.left, tag)
        self.apply(root.right, tag)
        root.lazy = 0

    def split(self, root: Node | None, key: int) -> tuple[Node | None, Node | None]:
        """Split into values < key and values >= key."""
        if root is None:
            return None, None

        self.pushdown(root)
        if root.val < key:
            a, b = self.split(root.right, key)
            root.right = a
            self.pushup(root)
            return root, b

        a, b = self.split(root.left, key)
        root.left = b
        self.pushup(root)
        return a, root

    def merge(self, a: Node | None, b: Node | None) -> Node | None:
        """Merge two trees where every value in a is <= every value in b."""
        if a is None or b is None:
            return a if a is not None else b

        if a.pri < b.pri:
            self.pushdown(a)
            a.right = self.merge(a.right, b)
            self.pushup(a)
            return a
        else:
            self.pushdown(b)
            b.left = self.merge(a, b.left)
            self.pushup(b)
            return b

    def add(self, root: Node | None, value: int) -> Node | None:
        """Insert one value. Duplicates are allowed."""
        a, b = self.split(root, value)
        mid = self.make(value)
        return self.merge(self.merge(a, mid), b)

    def remove(self, root: Node | None, value: int) -> Node | None:
        """Erase one occurrence of value if it exists."""
        if root is None:
            return None
        self.pushdown(root)
        if root.val == value:
            return self.merge(root.left, root.right)
        if value < root.val:
            root.left = self.remove(root.left, value)
        else:
            root.right = self.remove(root.right, value)
        self.pushup(root)
        return root

    def update(
        self, root: Node | None, left: int, right: int, value: int
    ) -> Node | None:
        """Add value to all keys in [left, right)."""
        a, b = self.split(root, left)
        c, d = self.split(b, right)
        self.apply(c, value)
        return self.merge(self.merge(a, c), d)

    def popmin(self, root: Node | None) -> Node | None:
        """Remove the minimum value from the tree."""
        if root is None:
            return None
        self.pushdown(root)
        if root.left is None:
            return root.right
        root.left = self.popmin(root.left)
        self.pushup(root)
        return root

    def popmax(self, root: Node | None) -> Node | None:
        """Remove the maximum value from the tree."""
        if root is None:
            return None
        self.pushdown(root)
        if root.right is None:
            return root.left
        root.right = self.popmax(root.right)
        self.pushup(root)
        return root

    def front(self, root: Node) -> int:
        """Return the minimum value. Requires root is not None."""
        self.pushdown(root)
        while root.left is not None:
            root = root.left
            self.pushdown(root)
        return root.val

    def back(self, root: Node) -> int:
        """Return the maximum value. Requires root is not None."""
        self.pushdown(root)
        while root.right is not None:
            root = root.right
            self.pushdown(root)
        return root.val

    def bisect_left(self, root: Node | None, key: int) -> int:
        """Return how many values are < key."""
        if root is None:
            return 0
        self.pushdown(root)
        if root.val < key:
            return self.size(root.left) + 1 + self.bisect_left(root.right, key)
        else:
            return self.bisect_left(root.left, key)

    def bisect_right(self, root: Node | None, key: int) -> int:
        """Return how many values are <= key."""
        if root is None:
            return 0
        self.pushdown(root)
        if root.val <= key:
            return self.size(root.left) + 1 + self.bisect_right(root.right, key)
        else:
            return self.bisect_right(root.left, key)

    def kth(self, root: Node, k: int) -> int:
        """Return the 0-indexed kth value."""
        self.pushdown(root)
        left_size = self.size(root.left)
        if k < left_size:
            return self.kth(root.left, k)
        elif k == left_size:
            return root.val
        else:
            return self.kth(root.right, k - left_size - 1)

    def predecessor(self, root: Node | None, key: int) -> int:
        """Return the largest value < key. Requires the answer to exist."""
        return self.kth(root, self.bisect_left(root, key) - 1)

    def successor(self, root: Node | None, key: int) -> int:
        """Return the smallest value > key. Requires the answer to exist."""
        return self.kth(root, self.bisect_right(root, key))


def solve() -> None:
    n = int(input())

    tr = FHQTreap()
    root = None

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


if __name__ == "__main__":
    solve()
