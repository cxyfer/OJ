t = int(input())
    
for _ in range(t):
    n, a, b = map(int, input().split())
    print("NO" if abs(a - b) & 1 else "YES")