"""
Reference:
- https://zhuanlan.zhihu.com/p/605710274
- https://www.luogu.com.cn/article/edsumipr
"""

n = int(input())

P = list(map(lambda x: int(x), input().split()))
Q = list(map(lambda x: int(x), input().split()))

A, B = [0] * (n + 1), [0] * (n + 1)
for i, (x, y) in enumerate(zip(P, Q), 1):
    A[x] = i
    B[y] = i

ans = 0
maxl = n + 1 # [1, mex - 1] 都出現的最大 l
minr = 0 # [1, mex - 1] 都出現的最小 r

# 枚舉 MEX 值
for mex in range(1, n + 1):
    """
    對於當前的 mex 值，需確保在區間 [l, r] 中，數字 1 到 mex-1 都出現，且 mex 未出現。
    - 因此，找到 mex 在 P 和 Q 中出現的最早位置，並更新 maxl 為這些位置的最小值，確保 l 不低於此位置。
    - 同時，找到 mex 在 P 和 Q 中出現的最晚位置，並更新 minr 為這些位置的最大值，確保 r 不小於此位置。
    """
    maxl = min(maxl, A[mex], B[mex])
    minr = max(minr, A[mex], B[mex])
    
    minl = 1
    maxr = n

    """
    若 mex < n，則還需確保在區間 [l, r] 中，mex 沒有出現。
    透過 mex+1 在 P 和 Q 中的位置進行判斷：
    - 如果 mex+1 在 P 中的位置小於 maxl，則 l 必須大於該位置，即 l >= A[mex+1] + 1。
    - 否則，r 必須小於該位置，即 r <= A[mex+1] - 1。
    - 同理，對排列 Q 進行同樣的判斷，更新 minl 和 maxr。
    """
    if mex < n:
        for pos in [A[mex + 1], B[mex + 1]]:
            if pos < maxl:
                minl = max(minl, pos + 1)
            else:
                maxr = min(maxr, pos - 1)

    # 計算合法區間數量    
    if maxl >= minl and maxr >= minr:
        ans += (maxl - minl + 1) * (maxr - minr + 1)

    """
    處理 mex = 1 的特殊情況
    - 當 mex = 1 時，代表在區間 [l, r] 中，數字 1 沒有出現，因此，滿足條件的區間必須不包含數字 1。
    - 找出數字 1 在 P 和 Q 中的位置，分別為 A[1] 和 B[1]。
    - 左邊界最大不能超過 A[1] 和 B[1] 之一的最小值。
    - 右邊界最大不能超過 n - A[1] 和 n - B[1] 的最小值。
    - 中間可能的間隔長度為 |A[1] - B[1]| - 1。
    - 將這三部分的數量加總後，累加到總答案 ans 中。
    """
    if mex == 1:
        l = min(A[mex] - 1, B[mex] - 1)
        r = min(n - A[mex], n - B[mex])
        m = abs(A[mex] - B[mex]) - 1

        ans += l * (l + 1) // 2
        ans += r * (r + 1) // 2
        ans += m * (m + 1) // 2

print(ans)