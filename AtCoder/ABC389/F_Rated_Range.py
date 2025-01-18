from atcoder.lazysegtree import LazySegTree

N = int(input())
contests = [tuple(map(int, input().split())) for _ in range(N)]
Q = int(input())
queries = [int(input()) for _ in range(Q)]

MX = max(max(r for _, r in contests), max(q for q in queries)) + 1
lst = LazySegTree(op=max,
                  e=0, 
                  mapping=lambda f, x: f+x,
                  composition=lambda f, g: f+g,
                  id_=0,
                  v=list(range(MX)))

for l, r in contests:
    l = lst.max_right(0, lambda x: x < l)
    r = lst.max_right(0, lambda x: x <= r)
    lst.apply(l, r, 1)

for q in queries:
    print(lst.get(q))