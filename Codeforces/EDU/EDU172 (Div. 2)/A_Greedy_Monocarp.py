from itertools import accumulate

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    
    s = list(accumulate(A, initial=0))
    
    m = 0
    for i in range(1, n + 1):
        if s[i] <= k:
            m = i
        else:
            break
    print(k - s[m])