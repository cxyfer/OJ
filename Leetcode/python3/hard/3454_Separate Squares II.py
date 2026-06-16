#
# @lc app=leetcode id=3454 lang=python3
#
# [3454] Separate Squares II
#


# @lcpr-template-start
from preImport import *
import typing

# @lcpr-template-end
"""
1. 如果只有一維，且「只加不減」，可以離散化後維護每一個線段，類似 [ABC435E](https://atcoder.jp/contests/abc435/tasks/abc435_e)
2. 考慮二維，可以||用掃描線轉換成在一維上的「有加有減」||，並使用支援區間修改資料結構維護
3. 從「只加不減」轉換到「有加有減」，可以維護最小覆蓋次數的長度，並檢查最小覆蓋次數是否大於0
"""


# @lc code=start
# from atcoder.lazysegtree import LazySegTree
class LazySegTree:
    def __init__(
        self,
        op: typing.Callable[[typing.Any, typing.Any], typing.Any],
        e: typing.Any,
        mapping: typing.Callable[[typing.Any, typing.Any], typing.Any],
        composition: typing.Callable[[typing.Any, typing.Any], typing.Any],
        id_: typing.Any,
        v: typing.Union[int, typing.List[typing.Any]],
    ) -> None:
        self._op = op
        self._e = e
        self._mapping = mapping
        self._composition = composition
        self._id = id_

        if isinstance(v, int):
            v = [e] * v

        self._n = len(v)
        self._log = self._n.bit_length()
        self._size = 1 << self._log
        self._d = [e] * (2 * self._size)
        self._lz = [self._id] * self._size
        for i in range(self._n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def set(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += self._size
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self, p: int) -> typing.Any:
        assert 0 <= p < self._n

        p += self._size
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        return self._d[p]

    def prod(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n

        if left == right:
            return self._e

        left += self._size
        right += self._size

        for i in range(self._log, 0, -1):
            if ((left >> i) << i) != left:
                self._push(left >> i)
            if ((right >> i) << i) != right:
                self._push(right >> i)

        sml = self._e
        smr = self._e
        while left < right:
            if left & 1:
                sml = self._op(sml, self._d[left])
                left += 1
            if right & 1:
                right -= 1
                smr = self._op(self._d[right], smr)
            left >>= 1
            right >>= 1

        return self._op(sml, smr)

    def all_prod(self) -> typing.Any:
        return self._d[1]

    def apply(
        self,
        left: int,
        right: typing.Optional[int] = None,
        f: typing.Optional[typing.Any] = None,
    ) -> None:
        assert f is not None

        if right is None:
            p = left
            assert 0 <= left < self._n

            p += self._size
            for i in range(self._log, 0, -1):
                self._push(p >> i)
            self._d[p] = self._mapping(f, self._d[p])
            for i in range(1, self._log + 1):
                self._update(p >> i)
        else:
            assert 0 <= left <= right <= self._n
            if left == right:
                return

            left += self._size
            right += self._size

            for i in range(self._log, 0, -1):
                if ((left >> i) << i) != left:
                    self._push(left >> i)
                if ((right >> i) << i) != right:
                    self._push((right - 1) >> i)

            l2 = left
            r2 = right
            while left < right:
                if left & 1:
                    self._all_apply(left, f)
                    left += 1
                if right & 1:
                    right -= 1
                    self._all_apply(right, f)
                left >>= 1
                right >>= 1
            left = l2
            right = r2

            for i in range(1, self._log + 1):
                if ((left >> i) << i) != left:
                    self._update(left >> i)
                if ((right >> i) << i) != right:
                    self._update((right - 1) >> i)

    def max_right(self, left: int, g: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= left <= self._n
        assert g(self._e)

        if left == self._n:
            return self._n

        left += self._size
        for i in range(self._log, 0, -1):
            self._push(left >> i)

        sm = self._e
        first = True
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            if not g(self._op(sm, self._d[left])):
                while left < self._size:
                    self._push(left)
                    left *= 2
                    if g(self._op(sm, self._d[left])):
                        sm = self._op(sm, self._d[left])
                        left += 1
                return left - self._size
            sm = self._op(sm, self._d[left])
            left += 1

        return self._n

    def min_left(self, right: int, g: typing.Any) -> int:
        assert 0 <= right <= self._n
        assert g(self._e)

        if right == 0:
            return 0

        right += self._size
        for i in range(self._log, 0, -1):
            self._push((right - 1) >> i)

        sm = self._e
        first = True
        while first or (right & -right) != right:
            first = False
            right -= 1
            while right > 1 and right % 2:
                right >>= 1
            if not g(self._op(self._d[right], sm)):
                while right < self._size:
                    self._push(right)
                    right = 2 * right + 1
                    if g(self._op(self._d[right], sm)):
                        sm = self._op(self._d[right], sm)
                        right -= 1
                return right + 1 - self._size
            sm = self._op(self._d[right], sm)

        return 0

    def _update(self, k: int) -> None:
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])

    def _all_apply(self, k: int, f: typing.Any) -> None:
        self._d[k] = self._mapping(f, self._d[k])
        if k < self._size:
            self._lz[k] = self._composition(f, self._lz[k])

    def _push(self, k: int) -> None:
        self._all_apply(2 * k, self._lz[k])
        self._all_apply(2 * k + 1, self._lz[k])
        self._lz[k] = self._id


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        Xs = set()
        for x, y, l in squares:  # [x, x + l)
            Xs.add(x)
            Xs.add(x + l)

        Xs = sorted(Xs)
        mapX = {x: i for i, x in enumerate(Xs)}
        # (min cover count, length of segments with min cover count)
        data = [(0, x2 - x1) for x1, x2 in pairwise(Xs)]

        op = lambda a, b: (a[0], a[1] + b[1]) if a[0] == b[0] else min(a, b)
        mapping = lambda f, s: (s[0] + f, s[1])
        composition = lambda f, g: f + g
        seg = LazySegTree(op, (float("inf"), 0), mapping, composition, 0, data)

        events = []
        for x, y, l in squares:
            events.append((y, x, x + l, 1))
            events.append((y + l, x, x + l, -1))
        events.sort(key=lambda x: x[0])

        tot_w = Xs[-1] - Xs[0]
        area = 0.0
        prev_y = events[0][0]
        records = []
        for y, l, r, d in events:
            curr_y = y
            if curr_y > prev_y:
                mn, ln = seg.all_prod()
                curr_w = tot_w - (ln if mn == 0 else 0)
                area += curr_w * (curr_y - prev_y)
                records.append((area, curr_w, curr_y))
            seg.apply(mapX[l], mapX[r], d)  # [l, r)
            prev_y = curr_y

        tgt = area / 2.0
        # for area, w, y1, y2 in records:
        #     if area >= tgt:
        #         return y2 - (area - tgt) / w
        idx = bisect_left(records, tgt, key=lambda x: x[0])
        area, w, y2 = records[idx]
        return y2 - (area - tgt) / w
# @lc code=end

sol = Solution()
print(sol.separateSquares([[0, 0, 1], [2, 2, 1]]))  # 1.00000
