N, K = map(int, input().split())
A = set(map(int, input().split()))

s = (1 + K) * K // 2
for x in A:
    if 1 <= x <= K:
        s -= x
print(s)