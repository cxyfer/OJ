T = int(input())

anss = []
for tc in range(1, T+1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    P.sort()
    ans = 0
    for i in range(N-1):
        cur = P[i][1]
        for j in range(i+1, N):
            if cur >= P[j][1]:
                ans += 1
    anss.append(ans)
print(*anss, sep='\n')