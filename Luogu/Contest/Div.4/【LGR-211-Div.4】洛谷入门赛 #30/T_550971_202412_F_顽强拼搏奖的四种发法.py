n, t, p, k = map(int, input().split())

ac = [[False] * (p + 1) for _ in range(t + 1)]
cnt = [0] * (t + 1)

ans = [-1, -1, -1, -1]
last = []
for _ in range(n):
    tid, pid, state = map(int, input().split())
    if state == 0:
        continue
    ans[0] = tid
    if not ac[tid][pid]:
        ans[1] = tid
        ac[tid][pid] = True
        last.append(tid)
        cnt[tid] += 1
        if cnt[tid] == 1:
            ans[3] = tid
while last and cnt[last[-1]] >= k:
    last.pop()
ans[2] = last[-1] if last else -1

print(*ans)