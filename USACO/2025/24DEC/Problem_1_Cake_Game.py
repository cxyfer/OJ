t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    tot = sum(A)
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + A[i]
    
    ln = n // 2 + 1
    ans = float('inf')
    for i in range(n - ln + 1):
        ans = min(ans, s[i + ln] - s[i])
    print(ans, tot - ans)