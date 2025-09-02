N, Q = map(int, input().split())
ans = N
teeth = [1] * N
queries = list(map(int, input().split()))
for q in queries:
    if teeth[q-1] == 1:
        teeth[q-1] = 0
        ans -= 1
    else:
        teeth[q-1] = 1
        ans += 1
print(ans)