t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    cnt = [0, 0]
    for x in A:
        cnt[x] += 1
    print(cnt[1] & 1, min(cnt[0], cnt[1]))