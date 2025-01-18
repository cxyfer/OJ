from heapq import heappush, heappop

n, m, t, k = map(int, input().split())

hp = []
info = [[() for _ in range(t + 1)] for _ in range(m + 1)]
for _ in range(n):
    team, s1, s2, s3, idx, rk = input().split()
    idx, rk = int(idx), int(rk)
    info[idx][rk] = (team, s1, s2, s3)
    heappush(hp, (rk, idx))

ans = []
vis = set()
while k and hp:
    rk, idx = heappop(hp)
    team, s1, s2, s3 = info[idx][rk]
    if s1 in vis or s2 in vis or s3 in vis:
        continue
    vis.update([s1, s2, s3])
    ans.append((team, s1, s2, s3))
    k -= 1

print(len(ans))
for team, s1, s2, s3 in ans:
    print(team, s1, s2, s3)