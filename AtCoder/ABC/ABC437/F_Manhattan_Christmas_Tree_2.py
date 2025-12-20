from atcoder.segtree import SegTree

fmax = lambda a, b : a if a > b else b
fmin = lambda a, b : a if a < b else b

def solve():
    n, q = map(int, input().split())
    P = [tuple(map(int, input().split())) for _ in range(n)]
    assert len(P) == n

    seg1 = SegTree(fmax, float('-inf'), [x + y for x, y in P])
    seg2 = SegTree(fmin, float('inf'), [x + y for x, y in P])
    seg3 = SegTree(fmax, float('-inf'), [x - y for x, y in P])
    seg4 = SegTree(fmin, float('inf'), [x - y for x, y in P])

    for _ in range(q):
        op, *args = map(int, input().split())
        if op == 1:
            i, x, y = args
            seg1.set(i - 1, x + y)
            seg2.set(i - 1, x + y)
            seg3.set(i - 1, x - y)
            seg4.set(i - 1, x - y)
        else:
            l, r, x, y = args
            max_s = seg1.prod(l - 1, r)
            min_s = seg2.prod(l - 1, r)
            max_d = seg3.prod(l - 1, r)
            min_d = seg4.prod(l - 1, r)
            print(max(max_s - (x + y), (x + y) - min_s, max_d - (x - y), (x - y) - min_d))

if __name__ == "__main__":
    solve()