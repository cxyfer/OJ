N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

arr = []
for i, x in enumerate(A):
    arr.append((x, 0))
for i, x in enumerate(B):
    arr.append((x, 1))
arr.sort()

flag = False
for i in range(N + M - 1):
    if 0 == arr[i][1] == arr[i + 1][1]:
        flag = True
        break
print("Yes" if flag else "No")