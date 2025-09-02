N, M = map(int, input().split())

st = set()

for _ in range(M):
    x, y = map(int, input().split())
    st.add((x, y))
    for dx, dy in [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]:
        nx, ny = x + dx, y + dy
        if 1 <= nx <= N and 1 <= ny <= N:
            st.add((nx, ny))

print(N * N - len(st))