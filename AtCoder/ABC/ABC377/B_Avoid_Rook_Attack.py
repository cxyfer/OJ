mp = [list(input()) for _ in range(8)]

row = [False] * 8
col = [False] * 8

for i in range(8):
    for j in range(8):
        if mp[i][j] == "#":
            row[i] = True
            col[j] = True

ans = 0
for i in range(8):
    for j in range(8):
        if not row[i] and not col[j]:
            ans += 1
print(ans)