from functools import cache

N = 11

@cache
def digsum(x):
    ans = 0
    while x:
        ans += x % 10
        x //= 10
    return ans

ans = 0
for i in range(N+1):
    for j in range(N+1):
        k = N - i - j
        if k < 0:
            break
        if digsum(i) + digsum(j) + digsum(k) == digsum(N):
            print(i, j, k)
            ans += 1

print(ans)

