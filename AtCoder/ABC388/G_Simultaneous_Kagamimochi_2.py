from atcoder.segtree import SegTree

N = int(input())
A = list(map(int, input().split()))

# 計算下一個符合條件的位置
nxt = [0] * N
right = 0
for i in range(N):
    while right < N and 2 * A[i] > A[right]:
        right += 1
    nxt[i] = right

# 計算每個位置與下一個符合條件的位置的間距
gaps = [nxt[i] - i for i in range(N)]
seg = SegTree(lambda x, y: max(x, y), -float('inf'), gaps)  # 維護區間內的最大間距

Q = int(input())
queries = [list(map(int, input().split())) for _ in range(Q)]
for (L, R) in queries:

    def check(k):
        return L + k - 1 + seg.prod(L - 1, L - 1 + k) <= R

    left, right = 0, (R - L + 1) // 2
    while left <= right:
        mid = (left + right) // 2
        # 查詢 [L, L+mid) 區間內的最大間距
        max_gap = seg.prod(L - 1, L - 1 + mid)  # 0-based
        """
            若區間內可以組成 K 對，則最小的 K 個數和最大的 K 個數必能配對成功，
            其中最小的 K 個數為 [L, L + K - 1]，最大的 K 個數為 [R - K + 1, R]。

            但若最小的 K 個數中有一個數無法配對成功，則會影響到後續的數，使後續的數需要往後遞移，
            因此其實考慮最小的 K 個數的右端點 L + K - 1 、以及 [L, L + K - 1] 的最大間距 max_gap 即可。
            
            如果 L + K - 1 + max_gap > R，則說明 K 太大，需要縮小
        """
        if check(mid):
            left = mid + 1
        else:
            right = mid - 1
    print(right)  # 越小越合法，求最大的合法值