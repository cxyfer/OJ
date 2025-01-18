import sys
input = lambda: sys.stdin.readline().strip()
print = lambda val: sys.stdout.write(str(val) + "\n")

MAXN = (1 << 16) + 5
is_prime = [True] * MAXN
is_prime[0] = is_prime[1] = False
for i in range(2, int(MAXN ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAXN, i):
            is_prime[j] = False
primes = [i for i in range(MAXN) if is_prime[i]]

while True:
    n = int(input())
    if n == 0:
        break
    ans = []
    if n < 0:
        ans.append(-1)
        x = -n
    else:
        x = n
    for p in primes:
        if p * p > x:
            break
        while x % p == 0:
            ans.append(p)
            x //= p
    if x > 1:
        ans.append(x)
    print(f"{n} = {' x '.join(map(str, ans))}")
