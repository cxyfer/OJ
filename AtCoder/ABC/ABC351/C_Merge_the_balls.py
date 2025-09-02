N = int(input())
A = list(map(int, input().split()))

B = [] # stack
for i in range(N):
    B.append(A[i])
    while len(B) >= 2 and B[-1] == B[-2]:
        tmp = B[-1]
        B.pop()
        B.pop()
        B.append(tmp + 1)
    # print(B)
print(len(B))