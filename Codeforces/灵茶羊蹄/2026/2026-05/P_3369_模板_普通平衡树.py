from __future__ import annotations
from random import getrandbits
from bisect import bisect_left, bisect_right, insort
# from sortedcontainers import SortedList

# fmt: off
import sys
it = iter(sys.stdin.read().splitlines())
def input():
    return next(it)
def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)) + end)
# fmt: on


class SortedList:
    def __init__(self, iterable=None, load_factor=1000):
        self._len = 0
        self._load = load_factor
        self._lists = []
        self._maxes = []
        self._index = []
        self._offset = 0
        if iterable is not None:
            self.update(iterable)

    def __len__(self):
        return self._len

    def _build_index(self):
        self._index = []
        if not self._lists:
            return
        row0 = [len(l) for l in self._lists]
        if len(row0) == 1:
            self._index[:] = row0
            self._offset = 0
            return
        head = iter(row0)
        row1 = [x + y for x, y in zip(head, head)]
        if len(row0) & 1:
            row1.append(row0[-1])
        if len(row1) == 1:
            self._index[:] = row1 + row0
            self._offset = 1
            return
        size = 2 ** ((len(row1) - 1).bit_length())
        row1.extend([0] * (size - len(row1)))
        tree = [row0, row1]
        while len(tree[-1]) > 1:
            head = iter(tree[-1])
            row = [x + y for x, y in zip(head, head)]
            tree.append(row)
        for row in reversed(tree):
            self._index.extend(row)
        self._offset = size * 2 - 1

    def _update_tree(self, pos, delta):
        if not self._index:
            return
        idx = self._offset + pos
        while idx:
            self._index[idx] += delta
            idx = (idx - 1) >> 1
        self._index[0] += delta

    def add(self, value):
        if not self._maxes:
            self._lists.append([value])
            self._maxes.append(value)
            self._len = 1
            return
        pos = bisect_right(self._maxes, value)
        if pos == len(self._maxes):
            pos -= 1
            self._lists[pos].append(value)
            self._maxes[pos] = value
        else:
            insort(self._lists[pos], value)
        self._len += 1
        if len(self._lists[pos]) > (self._load << 1):
            self._expand(pos)
        elif self._index:
            self._update_tree(pos, 1)

    def _expand(self, pos):
        _list = self._lists[pos]
        half = _list[self._load :]
        del _list[self._load :]
        self._maxes[pos] = _list[-1]
        self._lists.insert(pos + 1, half)
        self._maxes.insert(pos + 1, half[-1])
        self._index = []

    def discard(self, value):
        if not self._maxes:
            return
        pos = bisect_left(self._maxes, value)
        if pos == len(self._maxes):
            return
        idx = bisect_left(self._lists[pos], value)
        if self._lists[pos][idx] == value:
            self.pop(self._loc(pos, idx))

    def remove(self, value):
        if not self._maxes:
            raise ValueError
        pos = bisect_left(self._maxes, value)
        if pos == len(self._maxes):
            raise ValueError
        idx = bisect_left(self._lists[pos], value)
        if self._lists[pos][idx] == value:
            self.pop(self._loc(pos, idx))
        else:
            raise ValueError

    def __delitem__(self, index):
        self.pop(index)

    def __getitem__(self, index):
        if isinstance(index, slice):
            start, stop, step = index.indices(self._len)
            if step == 1 and start < stop:  # Optimization for simple slice
                if start == 0 and stop == self._len:
                    return [x for l in self._lists for x in l]
                start_pos, start_idx = self._pos(start)
                start_list = self._lists[start_pos]
                if len(start_list) >= start_idx + stop - start:
                    return start_list[start_idx : start_idx + stop - start]
                res = start_list[start_idx:]
                stop_pos, stop_idx = self._pos(stop)
                for i in range(start_pos + 1, stop_pos):
                    res += self._lists[i]
                if stop_idx:
                    res += self._lists[stop_pos][:stop_idx]
                return res
            return [self[i] for i in range(start, stop, step)]
        pos, idx = self._pos(index)
        return self._lists[pos][idx]

    def __contains__(self, value):
        if not self._maxes:
            return False
        pos = bisect_left(self._maxes, value)
        if pos == len(self._maxes):
            return False
        idx = bisect_left(self._lists[pos], value)
        return self._lists[pos][idx] == value

    def pop(self, index=-1):
        pos, idx = self._pos(index)
        val = self._lists[pos][idx]
        del self._lists[pos][idx]
        self._len -= 1
        if len(self._lists[pos]) > (self._load >> 1):
            self._maxes[pos] = self._lists[pos][-1]
            if self._index:
                self._update_tree(pos, -1)
        else:
            self._delete(pos, idx)
        return val

    def _delete(self, pos, idx):
        if len(self._lists) > 1:
            if not pos:
                pos += 1
            prev = pos - 1
            self._lists[prev].extend(self._lists[pos])
            self._maxes[prev] = self._lists[prev][-1]
            del self._lists[pos]
            del self._maxes[pos]
            self._index = []
            if len(self._lists[prev]) > (self._load << 1):
                self._expand(prev)
        elif self._lists[pos]:
            self._maxes[pos] = self._lists[pos][-1]
        else:
            del self._lists[pos]
            del self._maxes[pos]
            self._index = []

    def _loc(self, pos, idx):
        if not pos:
            return idx
        if not self._index:
            self._build_index()
        total = 0
        idx_pos = self._offset + pos
        while idx_pos:
            if not idx_pos & 1:
                total += self._index[idx_pos - 1]
            idx_pos = (idx_pos - 1) >> 1
        return total + idx

    def _pos(self, index):
        if index < 0:
            index += self._len
        if index < 0 or index >= self._len:
            raise IndexError
        if index < len(self._lists[0]):
            return 0, index
        if not self._index:
            self._build_index()
        pos = 0
        child = 1
        len_index = len(self._index)
        while child < len_index:
            index_child = self._index[child]
            if index < index_child:
                pos = child
            else:
                index -= index_child
                pos = child + 1
            child = (pos << 1) + 1
        return (pos - self._offset, index)

    def bisect_left(self, value):
        if not self._maxes:
            return 0
        pos = bisect_left(self._maxes, value)
        if pos == len(self._maxes):
            return self._len
        idx = bisect_left(self._lists[pos], value)
        return self._loc(pos, idx)

    def bisect_right(self, value):
        if not self._maxes:
            return 0
        pos = bisect_right(self._maxes, value)
        if pos == len(self._maxes):
            return self._len
        idx = bisect_right(self._lists[pos], value)
        return self._loc(pos, idx)

    def count(self, value):
        return self.bisect_right(value) - self.bisect_left(value)

    def update(self, iterable):
        for x in iterable:
            self.add(x)

    def __iter__(self):
        for l in self._lists:
            yield from l

    def __repr__(self):
        return str(list(self))


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


def solve1():
    q = int(input())
    sl = SortedList()
    for _ in range(q):
        op, x = map(int, input().split())
        if op == 1:
            sl.add(x)
        elif op == 2:
            sl.remove(x)
        elif op == 3:
            print(sl.bisect_left(x) + 1)
        elif op == 4:
            print(sl[x - 1])
        elif op == 5:
            print(sl[sl.bisect_left(x) - 1])
        elif op == 6:
            print(sl[sl.bisect_right(x)])


def solve2() -> None:
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


# solve = solve1
solve = solve2

if __name__ == "__main__":
    solve()
