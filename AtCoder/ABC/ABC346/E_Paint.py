from collections import defaultdict
H, W, M = map(int, input().split())

ops = [list(map(int, input().split())) for _ in range(M)]

cnt = defaultdict(int)
cnt[0] = H * W
row, col = set(), set() # 紀錄哪些行列被確定了 
for t, a, x in ops[::-1]: # 倒過來處理，可以確定哪些地方的顏色
    if t == 1: # row
        if a in row:
            continue
        row.add(a)
        num = W - len(col)
        cnt[x] += num
        cnt[0] -= num
    else: # col
        if a in col:
            continue
        col.add(a)
        num = H - len(row)
        cnt[x] += num
        cnt[0] -= num
print(sum([1 if v else 0 for v in cnt.values()]))
for k, v in sorted(cnt.items()):
    if v == 0:
        continue
    print(k, v)


