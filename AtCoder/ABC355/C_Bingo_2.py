N, T = map(int, input().split())
A = list(map(int, input().split()))

rows, cols = [0] * N, [0] * N
diag = [0] * 2

for i, x in enumerate(A):
    r = (x - 1) // N
    c = (x - 1) % N
    rows[r] += 1
    cols[c] += 1
    if r == c:
        diag[0] += 1
    if r + c == N - 1:
        diag[1] += 1
    if rows[r] == N or cols[c] == N or diag[0] == N or diag[1] == N:
        print(i + 1)
        break
else:
    print(-1)