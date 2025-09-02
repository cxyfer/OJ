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
                  v=list(range(MX))  # 初始值是當前 index 對應的 rating
                  )

for l, r in contests:
    # 找到最小的 j 使得 f[j] >= l
    l = lst.max_right(0, lambda x: x < l)
    # 找到最小的 j 使得 f[j] > r，其前一個位置即是最大的 j 使得 f[j] <= r
    r = lst.max_right(0, lambda x: x <= r)
    lst.apply(l, r, 1)  # 將 [l, r) 的 rating 增加 1

for q in queries:
    print(lst.get(q))
