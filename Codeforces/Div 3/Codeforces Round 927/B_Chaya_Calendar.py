from math import ceil
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    ans = 0

    for i in range(n):
        k = ceil((ans+1) / arr[i])
        ans = arr[i] * k
        
    print(ans)