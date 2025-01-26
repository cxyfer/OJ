N = int(input())
A = list(map(int, input().split()))

for i in range(N - 1):
    # if A[i + 1] / A[i] != A[1] / A[0]:
    if A[i + 1] * A[0] != A[1] * A[i]:
        print("No")
        break
else:
    print("Yes")