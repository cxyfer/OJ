import sys
input = lambda: sys.stdin.readline().strip()
print = lambda val: sys.stdout.write(str(val) + "\n")

MAXN = int(1e7) + 5
is_prime = [True] * MAXN
is_prime[0] = is_prime[1] = False
primes = []
for i in range(2, int(MAXN ** 0.5) + 1):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * i, MAXN, i):
            is_prime[j] = False

"""
哥德巴赫猜想：
任一大於2的偶數，都可表示成兩個質數之和。
"""

while True:
    try:
        n = int(input())
    except:
        break
    if n < 8:
        print("Impossible.")
        continue
    f1 = f2 = f3 = f4 = 0
    if n & 1:
        f1, f2 = 2, 3
        n -= 5
    else:
        f1, f2 = 2, 2
        n -= 4
    for p in primes:
        if p >= n:
            break
        if n - p > 0 and is_prime[n - p]:
            f3, f4 = p, n - p
            break
    print(f"{f1} {f2} {f3} {f4}")