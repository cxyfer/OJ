"""
B. Random
https://ac.nowcoder.com/acm/contest/120563/B

預處理質數篩 + 質因數分解
然而正解是利用數據的均勻分布性質，隨機化。
"""
from math import sqrt, gcd
from collections import defaultdict

MAX_N = int(sqrt(int(1e9)) + 5)
is_prime = [True] * MAX_N
is_prime[0] = is_prime[1] = False
for i in range(2, int(sqrt(MAX_N)) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX_N, i):
            is_prime[j] = False
primes = [i for i in range(MAX_N) if is_prime[i]]

def factorize(x: int):
    for p in primes:
        if p * p > x:
            break
        if x % p == 0:
            yield p
            while x % p == 0:
                x //= p
    if x > 1:
        yield x

def solve1():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n

    mp = defaultdict(int)
    for x in A:
        for f in factorize(x):
            if mp[f]:
                print(mp[f], x)
                return
            mp[f] = x
    print(-1)

def solve2():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n

    N = 1000
    for i in range(min(N, n)):
        for j in range(i + 1, min(N, n)):
            if gcd(A[i], A[j]) > 1:
                print(A[i], A[j])
                return
    print(-1)

# solve = solve1
solve = solve2

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()