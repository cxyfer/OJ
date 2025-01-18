N, Q = map(int, input().split())
C = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(Q)]

sets = [set([color]) for color in C]

for x, y in queries:
    x -= 1
    y -= 1
    if len(sets[x]) > len(sets[y]):
        sets[x], sets[y] = sets[y], sets[x]
    sets[y] |= sets[x]
    sets[x].clear()
    print(len(sets[y]))