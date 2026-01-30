from atcoder.segtree import SegTree

def solve():
    N = int(input())
    H = list(map(int, input().split()))
    A = list(map(int, input().split()))
    
    # seg[h] = 以高度 h 結尾的子序列最大美麗值
    seg = SegTree(max, 0, N + 1)
    for h, x in zip(H, A):
        f = seg.prod(0, h) + x  # 查詢高度 < h 的最大值，加上當前美麗值
        seg.set(h, max(seg.get(h), f))  # 更新以高度 h 結尾的最佳結果
    print(seg.all_prod())

if __name__ == "__main__":
    solve()