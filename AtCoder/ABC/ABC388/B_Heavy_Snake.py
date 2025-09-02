N, D = map(int, input().split())
snakes = [list(map(int, input().split())) for _ in range(N)]

for k in range(1, D + 1):
    ans = -float('inf')
    for i, (Ti, Li) in enumerate(snakes):
        ans = max(ans, (Li + k) * Ti)
    print(ans)