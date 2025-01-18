n, p = map(int, input().split())

vis = [False] * p
for _ in range(n):
    pid, state = map(int, input().split())
    if state == 1:
        vis[pid - 1] = True

print(sum(vis))