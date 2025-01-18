M, N, L = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
L = [list(map(int, input().split())) for _ in range(L)]

limits = set()
for x, y in L:
    limits.add((x-1, y-1))

mains = [(val, idx) for idx, val in enumerate(A)]
sides = [(val, idx) for idx, val in enumerate(B)]

mains.sort(key=lambda x: x[0], reverse=True)
sides.sort(key=lambda x: x[0], reverse=True)

ans = 0
for i in range(M):
    flag = False
    for j in range(N):
        x, y = mains[i][1], sides[j][1]
        if (x, y) in limits:
            flag = True
            continue
        ans = max(ans, mains[i][0] + sides[j][0])
        break
    if not flag:
        break
print(ans)
