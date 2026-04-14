from atcoder.lazysegtree import LazySegTree


def solve():
    n = int(input())
    W = list(map(int, input().split()))

    # S = (sz, lr, wr)
    # sz : 包含的元素(區間)個數
    # lr : 最右端元素對應區間的左端點
    # wr : 最右端元素對應區間的長度
    e = (0, 0, 0)

    def op(a, b):
        sz_a, lr_a, wr_a = a
        sz_b, lr_b, wr_b = b
        if sz_b == 0:
            return a
        return (sz_a + sz_b, lr_b, wr_b)

    # F = (mode, c)
    # mode = 1  : L <- c
    # mode = 2  : L <- c - W
    id_ = (0, 0)

    def mapping(f, s):
        mode, c = f
        sz, lr, wr = s
        if sz == 0 or mode == 0:
            return s
        return (sz, c if mode == 1 else c - wr, wr)

    def composition(f, g):
        # 新操作 f 蓋掉舊操作 g
        return f if f[0] else g

    data = [(1, 0, w) for w in W]
    seg = LazySegTree(op, e, mapping, composition, id_, data)

    ans = []

    q = int(input())
    for _ in range(q):
        t, *args = map(int, input().split())

        if t == 1:
            v = args[0] - 1
            lv = seg.get(v)[1]
            seg.apply(0, v + 1, (1, lv))  # apply to [0, v + 1)
        elif t == 2:
            v = args[0] - 1
            lv = seg.get(v)[1]
            rv = lv + W[v]
            seg.apply(0, v + 1, (2, rv))
        else:
            x = args[0]

            # 找到第一個包含 x + 0.5 的區間位置
            def check(s):
                _, lr, wr = s
                return not (lr <= x and x + 1 <= lr + wr)

            r = seg.max_right(0, check)
            ans.append(n - r)  # [r, n) 對應的區間皆包含 x + 0.5

    print(*ans, sep="\n")


if __name__ == "__main__":
    solve()
