import bisect

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
sum_A = sum(A)
R = K - sum_A # 剩餘的票數

sorted_A = sorted(A)
prefix_sum = [0]
for a in sorted_A:
    prefix_sum.append(prefix_sum[-1] + a)

result = []
for idx in range(N):
    A_i = A[idx]
    # Binary search for X in [0, R]
    left = 0
    right = R
    answer = -1
    while left <= right:
        mid = (left + right) // 2
        T = A_i + mid
        pos = bisect.bisect_right(sorted_A, T)
        c1 = N - pos
        # Calculate k_max
        C = T + 1
        budget = R - mid
        # Binary search for k_max in [0, pos]
        low_k = 0
        high_k = pos
        k_max = 0
        while low_k <= high_k:
            mid_k = (low_k + high_k) // 2
            required = C * mid_k - prefix_sum[mid_k]
            if required <= budget:
                k_max = mid_k
                low_k = mid_k + 1
            else:
                high_k = mid_k - 1
        total = c1 + k_max
        if total < M:
            answer = mid
            right = mid -1
        else:
            left = mid +1
    if answer != -1 and answer <= R:
        result.append(str(answer))
    else:
        result.append("-1")
print(' '.join(result))