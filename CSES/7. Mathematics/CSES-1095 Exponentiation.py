MOD = int(1e9 + 7)

def my_pow(a, b, MOD):
    res = 1
    while b:
        if b & 1:
            res = res * a % MOD
        a = a * a % MOD
        b >>= 1
    return res

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(my_pow(a, b, MOD))