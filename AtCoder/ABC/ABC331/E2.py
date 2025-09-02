from bisect import bisect_left

def solve() -> int:
    M, N, L = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    L = [list(map(int, input().split())) for _ in range(L)]

    limits = set()
    for x, y in L:
        limits.add((x-1, y-1))

    arrA = [(val, idx) for idx, val in enumerate(A)]
    arrB = [(val, idx) for idx, val in enumerate(B)]
    arrA.sort(key=lambda x: x[0])
    arrB.sort(key=lambda x: x[0])

    if (arrA[-1][1], arrB[-1][1]) not in limits:
        return arrA[-1][0] + arrB[-1][0]
    ans = 0
    for (i, j) in limits:
        x = bisect_left(arrA, (A[i], i)) # 二分查找 A[i] 在 arrA 中的位置 x
        y = bisect_left(arrB, (B[j], j)) # 二分查找 B[j] 在 arrB 中的位置 y
        if x > 0 and (arrA[x - 1][1], j) not in limits: # (x - 1, y) 不在限制中
            ans = max(ans, arrA[x - 1][0] + B[j])
        if y and (i, arrB[y - 1][1]) not in limits: # (x, y - 1) 不在限制中
            ans = max(ans, A[i] + arrB[y - 1][0])
    return ans

if __name__ == "__main__":
    print(solve())