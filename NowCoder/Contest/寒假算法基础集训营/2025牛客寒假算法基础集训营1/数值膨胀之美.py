import typing
# from atcoder.segtree import SegTree

class SegTree:
    def __init__(self,
                 op: typing.Callable[[typing.Any, typing.Any], typing.Any],
                 e: typing.Any,
                 v: typing.Union[int, typing.List[typing.Any]]) -> None:
        self._op = op
        self._e = e

        if isinstance(v, int):
            v = [e] * v

        self._n = len(v)
        self._log = self._n.bit_length()
        self._size = 1 << self._log
        self._d = [e] * (2 * self._size)

        for i in range(self._n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def prod(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n
        sml = self._e
        smr = self._e
        left += self._size
        right += self._size

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

    def _update(self, k: int) -> None:
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])
 
n = int(input())
A = list(map(int, input().split()))

pos = [(A[i], i) for i in range(n)]
pos.sort()

op = lambda x, y: (max(x[0], y[0]), min(x[1], y[1]))
e = (-float('inf'), float('inf'))
st = SegTree(op, e, [(v, v) for v in A])

ans = float('inf')
l = r = pos[0][1]
for val, pos in pos:
    l = min(l, pos)
    r = max(r, pos)

    mid = st.prod(l, r + 1)
    if l > 0:
        left = st.prod(0, l)
    else:
        left = (-float('inf'), float('inf'))
        
    if r < n - 1:
        right = st.prod(r + 1, n)
    else:
        right = (-float('inf'), float('inf'))
        
    mx = max(left[0], mid[0] * 2, right[0])
    mn = min(left[1], mid[1] * 2, right[1])
    ans = min(ans, mx - mn)
    
print(ans)