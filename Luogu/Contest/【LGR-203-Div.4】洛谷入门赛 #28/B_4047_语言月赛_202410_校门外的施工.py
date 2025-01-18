m, n = map(int, input().split())

tr = [0] + [1] * m
gr = [0] + [1] * (m - 1) + [0]

for _ in range(n):
    op, l, r = map(int, input().split())
    if op == 1:
        for i in range(l + 1, r):
            tr[i] = 0
        for i in range(l, r):
            gr[i] = 0
    else:
        for i in range(l, r + 1):
            tr[i] = 0
        for i in range(l, r):
            gr[i] = 0

print(sum(tr), sum(gr))