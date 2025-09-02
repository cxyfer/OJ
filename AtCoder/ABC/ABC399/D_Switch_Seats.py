T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    pos = [[] for _ in range(N + 1)]
    for i, x in enumerate(A, start=1):
        pos[x].append(i)

    ans = 0
    st = set()
    for x in range(1, N+1):
        a, b = pos[x]
        if (abs(b - a) == 1): continue
        st.add((a, b))

        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            if (a + dx, b + dy) in st:
                ans += 1
    print(ans)