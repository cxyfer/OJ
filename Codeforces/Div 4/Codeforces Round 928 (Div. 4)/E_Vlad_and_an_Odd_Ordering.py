t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    i = 1
    cur = n // 2 + (n&1)
    while cur < k:
        k -= cur 
        i = i*2
        n = n // 2
        cur = n // 2 + (n&1)
    print( (2*k - 1)*i )
