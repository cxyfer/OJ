from bisect import bisect_left, bisect_right, insort

"""
基於模仿的 sortedcontainers 的 SortedList，實現 SortedSet
但除非必要，否則還是優先使用 sortedcontainers 的 SortedList/SortedSet/SortedDict
"""
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
        half = _list[self._load:]
        del _list[self._load:]
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
                    return start_list[start_idx: start_idx + stop - start]
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

class SortedSet:
    def __init__(self, iterable=None, load_factor=1000):
        self._set = set()
        self._list = SortedList(load_factor=load_factor)
        if iterable is not None:
            self.update(iterable)

    def __len__(self):
        return len(self._set)

    def __contains__(self, value):
        return value in self._set

    def __iter__(self):
        return iter(self._list)

    def __getitem__(self, index):
        return self._list[index]

    def __delitem__(self, index):
        self.pop(index)

    def __repr__(self):
        return f"SortedSet({list(self._list)})"

    def add(self, value):
        if value not in self._set:
            self._set.add(value)
            self._list.add(value)
            return True
        return False

    def discard(self, value):
        if value in self._set:
            self._set.remove(value)
            self._list.discard(value)
            return True
        return False

    def remove(self, value):
        if value in self._set:
            self._set.remove(value)
            self._list.remove(value)
        else:
            raise ValueError(f"{value} not in SortedSet")

    def pop(self, index=-1):
        # 注意：這裡的 index 是排序後的索引，而非值
        val = self._list.pop(index)
        self._set.remove(val)
        return val

    def update(self, iterable):
        for x in iterable:
            self.add(x)

    def bisect_left(self, value):
        return self._list.bisect_left(value)

    def bisect_right(self, value):
        return self._list.bisect_right(value)

    def index(self, value):
        if value not in self._set:
            raise ValueError(f"{value} not in SortedSet")
        return self._list.bisect_left(value)

    def clear(self):
        self._set.clear()
        self._list = SortedList(load_factor=self._list._load)