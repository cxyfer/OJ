t = int(input())

for kase in range(1, t + 1):
    input()
    n = int(input())
    jobs = []
    for i in range(1, n + 1):
        a, b = map(int, input().split())
        jobs.append((a, b, i))
    jobs.sort(key=lambda x: x[1] / x[0], reverse=True)
    ans = []
    for i in range(n):
        ans.append(jobs[i][2])
    print(*ans)
    if kase < t:
        print()
