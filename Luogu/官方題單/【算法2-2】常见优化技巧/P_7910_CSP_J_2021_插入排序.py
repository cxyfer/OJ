"""
P7910 [CSP-J 2021] 插入排序
https://www.luogu.com.cn/problem/P7910

1. BIT + SortedList

在題目的排序方式下，A[i] 排序後的位置為：比 A[i] 小的元素個數 + A[i] 左側相同值的元素個數 + 1
第一項可以離散化後用 BIT 維護，第二項可以用 SortedList 維護。

2. 暴力

但操作 1 的數量最多為 5000，因此暴力維護即可。
對 (val, idx) 的 Tuple 進行排序，可以維護 pos 陣列，pos[idx] 表示原本在 idx 的元素排序後的位置。

對於操作 1，可以依照新值與舊值的大小關係，決定是往左還是往右移動。
每次交換相鄰的元素時，需要維護排序後的陣列以及 pos 陣列
"""

from collections import defaultdict
from bisect import bisect_left, bisect_right, insort
# from sortedcontainers import SortedList


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


class BIT:  # PURQ, 1-based
    __slots__ = ["tree"]

    def __init__(self, n: int):
        self.tree = [0] * (n + 1)

    def add(self, k: int, x: int) -> None:  # 令 nums[k] += x
        while k < len(self.tree):
            self.tree[k] += x
            k += k & -k

    def preSum(self, k: int) -> int:  # 求 nums[:k+1] 之和
        res = 0
        while k > 0:
            res += self.tree[k]
            k -= k & -k
        return res

    def query(self, l: int, r: int) -> int:  # 求 nums[l:r+1] 之和
        if l > r:
            return 0
        return self.preSum(r) - self.preSum(l - 1)


def solve1():
    n, q = map(int, input().split())
    A = list(map(int, input().split()))
    queries = [tuple(map(int, input().split())) for _ in range(q)]
    assert len(A) == n

    # 離散化
    Xs = set(A) | set(query[2] for query in queries if query[0] == 1)
    m = len(Xs)
    Xs = sorted(Xs)
    mp = {x: i for i, x in enumerate(Xs, start=1)}

    bit = BIT(m + 1)
    for x in A:
        bit.add(mp[x], 1)

    pos = defaultdict(SortedList)
    for i, x in enumerate(A):
        pos[x].add(i)

    for query in queries:
        op, *args = query
        if op == 1:
            idx, v = args[0] - 1, args[1]
            bit.add(mp[A[idx]], -1)
            bit.add(mp[v], 1)
            pos[A[idx]].remove(idx)
            pos[v].add(idx)
            A[idx] = v
        else:
            idx = args[0] - 1
            print(bit.preSum(mp[A[idx]] - 1) + pos[A[idx]].bisect_left(idx) + 1)


def solve2():
    n, q = map(int, input().split())
    A = list(map(int, input().split()))
    assert len(A) == n

    B = [(x, idx) for idx, x in enumerate(A)]
    B.sort()
    pos = [-1] * n
    for i, (_, idx) in enumerate(B):
        pos[idx] = i

    def swap(i, j):
        pos[B[i][1]], pos[B[j][1]] = pos[B[j][1]], pos[B[i][1]]
        B[i], B[j] = B[j], B[i]

    for _ in range(q):
        op, *args = map(int, input().split())
        if op == 1:
            idx, v = args[0] - 1, args[1]
            B[pos[idx]] = (v, idx)
            if v > A[idx]:
                i = pos[idx]
                while i + 1 < n and B[i + 1] < B[i]:
                    swap(i, i + 1)
                    i += 1
            else:
                i = pos[idx]
                while i - 1 >= 0 and B[i - 1] > B[i]:
                    swap(i, i - 1)
                    i -= 1
            A[idx] = v
        else:
            idx = args[0] - 1
            print(pos[idx] + 1)  # 1-indexed


solve = solve1
# solve = solve2

if __name__ == "__main__":
    solve()
