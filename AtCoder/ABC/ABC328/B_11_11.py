N = int(input())
D = list(map(int, input().split()))

ans = 0

for m in range(1, N+1):
    for d in range(1, D[m-1]+1):
        s = str(m) + str(d)
        if s.count(s[0]) == len(s):
            ans += 1
print(ans)

