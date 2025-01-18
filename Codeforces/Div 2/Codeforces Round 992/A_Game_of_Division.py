t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    pos = [[] for _ in range(k)]
    for i, x in enumerate(A):
        pos[x % k].append(i + 1)

    for i in range(k):
        if len(pos[i]) == 1:
            print("YES")
            print(pos[i][0])
            break
    else:
        print("NO")