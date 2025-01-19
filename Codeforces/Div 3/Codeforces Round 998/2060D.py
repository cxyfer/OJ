t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))

    for i in range(n - 1):
        if A[i] <= A[i + 1]:
            A[i + 1] -= A[i]
            A[i] = 0
            
    print("YES" if all(A[i] <= A[i + 1] for i in range(n - 1)) else "NO")