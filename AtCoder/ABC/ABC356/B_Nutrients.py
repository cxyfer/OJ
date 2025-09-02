N, M = map(int, input().split())
A = list(map(int, input().split()))

for _ in range(N):
    for i, x in enumerate(list(map(int, input().split()))):
        A[i] -= x

print("Yes" if all(x <= 0 for x in A) else "No")