N = int(input())
A = list(map(int, input().split()))
ST = [list(map(int, input().split())) for _ in range(N-1)]

for i in range(N-1):
    k = A[i] // ST[i][0]
    A[i] -= k * ST[i][0]
    A[i+1] += k * ST[i][1]

print(A[-1])