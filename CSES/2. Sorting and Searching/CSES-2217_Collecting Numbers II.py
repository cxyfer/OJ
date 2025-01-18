n, q = map(int, input().split())
A = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(q)]

pos = [-1] * (n + 1)
for i, x in enumerate(A):
    pos[x] = i

tot = 1
for x in range(2, n + 1):
    if pos[x - 1] > pos[x]:  # 需要額外一輪才能收集到 x
        tot += 1

for (a, b) in queries:
    a, b = a - 1, b - 1

    x, y = A[a], A[b]
    if x > y:
        x, y = y, x

    # 交換前
    if x - 1 > 0 and pos[x - 1] > pos[x]:
        tot -= 1
    if x + 1 <= n and pos[x] > pos[x + 1]:
        tot -= 1
    if y - 1 > 0 and y != x + 1 and pos[y - 1] > pos[y]:
        tot -= 1
    if y + 1 <= n and pos[y] > pos[y + 1]:
        tot -= 1

    # 交換
    A[a], A[b] = A[b], A[a]
    pos[A[a]], pos[A[b]] = a, b

    # 交換後
    if x - 1 > 0 and pos[x - 1] > pos[x]:
        tot += 1
    if x + 1 <= n and pos[x] > pos[x + 1]:
        tot += 1
    if y - 1 > 0 and y != x + 1 and pos[y - 1] > pos[y]:
        tot += 1
    if y + 1 <= n and pos[y] > pos[y + 1]:
        tot += 1

    print(tot)