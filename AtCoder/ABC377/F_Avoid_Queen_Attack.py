"""
    先使用集合記錄有哪些橫列、直行、主對角線、副對角線上有皇后

    若只考慮橫列和直行，則剩下 (n - len(row)) * (n - len(col)) 個位置可以放皇后

    接著考慮主對角線，其長度為 n - abs(d)，d 為主對角線的斜率。
    但主對角線可能與橫列、直行有相交，因此需要扣掉這些相交的點。
    這裡使用 overlaps 紀錄哪些橫列上發生了相交

    最後考慮副對角線，其長度為 n - abs(n + 1 - d)，d 為副對角線的斜率。
    但副對角線可能與橫列、直行、主對角線有相交，因此需要扣掉這些相交的點。
    這裡使用 overlaps 紀錄哪些橫列上發生了相交
"""

n, m = map(int, input().split())
row, col, diag1, diag2 = set(), set(), set(), set()

for _ in range(m):
    x, y = map(int, input().split())
    row.add(x)
    col.add(y)
    diag1.add(x - y)
    diag2.add(x + y)

ans = (n - len(row)) * (n - len(col))

for d1 in diag1: # d = x - y
    overlaps = set()
    for x in row:
        y = x - d1
        if 1 <= y <= n:
            overlaps.add(x)
    for y in col:
        x = y + d1
        if 1 <= x <= n:
            overlaps.add(x)
    d_len = n - abs(d1) # 對角線長度
    ans -= d_len - len(overlaps)

for d2 in diag2: # d = x + y
    overlaps = set()
    for x in row:
        y = d2 - x
        if 1 <= y <= n:
            overlaps.add(x)
    for y in col:
        x = d2 - y
        if 1 <= x <= n:
            overlaps.add(x)
    for d1 in diag1:
        x = (d2 + d1) / 2
        y = (d2 - d1) / 2
        if ((d2 + d1) % 2 == 0 and 1 <= x <= n and 1 <= y <= n):
            overlaps.add(x)
    d_len = n - abs((n + 1) - d2) # 對角線長度
    ans -= d_len - len(overlaps)

print(ans)
