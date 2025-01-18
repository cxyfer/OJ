MAX_N = int(1e5 + 5)
is_prime = [True] * MAX_N
is_prime[0] = is_prime[1] = False
for i in range(2, MAX_N):
    if is_prime[i]:
        for j in range(i * i, MAX_N, i):
            is_prime[j] = False

n, m, r, k = map(int, input().split())

cnt = 0
for x in range(n, 1, -1):
    if is_prime[x] and x % m == r:
        cnt += 1
    if cnt == k:
        print(x)
        break
else:
    print(-1)