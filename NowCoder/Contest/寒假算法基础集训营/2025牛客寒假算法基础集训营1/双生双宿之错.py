t = int(input())

def median(arr):
    m = len(arr)
    return arr[m // 2]

def cost(arr, v):
    return sum(abs(x - v) for x in arr)

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    m = n // 2
    p, q = median(A[:m]), median(A[m:])
    

    if all(x == A[0] for x in A):
        print(n // 2)
        continue

    if p != q:
        ans = cost(A[:m], p) + cost(A[m:], q)
    else:
        cost1 = cost(A[:m], p - 1) + cost(A[m:], p)
        cost2 = cost(A[:m], p) + cost(A[m:], p + 1)
        ans = min(cost1, cost2)
    print(ans)
