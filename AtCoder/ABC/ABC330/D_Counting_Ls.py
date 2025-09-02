N = int(input())
M = [ input() for _ in range(N) ]

rows = [0] * N 
cols = [0] * N

for i in range(N):
    for j in range(N):
        if M[i][j] == 'o':
            rows[i] += 1
            cols[j] += 1

ans = 0
for i in range(N):
    for j in range(N):
        if M[i][j] == 'o':
            # print(i, j, rows[i], cols[j])
            if rows[i] > 1 and cols[j] > 1:
                ans += (rows[i] - 1) * (cols[j] - 1)
print(ans)