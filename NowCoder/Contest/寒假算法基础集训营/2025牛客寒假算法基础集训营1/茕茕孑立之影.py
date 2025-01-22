t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    print(-1 if any(a == 1 for a in A) else int(1e9 + 7))