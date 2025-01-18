from math import gcd

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    
    g = gcd(*A)
    cnt = sum([x // g - 1 for x in A])

    print("YES" if cnt <= k else "NO")