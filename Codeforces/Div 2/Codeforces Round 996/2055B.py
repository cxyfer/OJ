t = int(input())
    
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    s_a, s_b = sum(A), sum(B)

    if n <= 2:
        print("YES" if s_a >= s_b else "NO")
        continue

    if s_a < s_b:
        print("NO")
        continue

    need = []
    for i in range(n):
        if B[i] > A[i]:
            need.append(B[i] - A[i])
    
    if len(need) > 1:
        print("NO")
        continue

    if len(need) == 0:
        print("YES")
        continue
    
    have = float('inf')
    for i in range(n):
        if A[i] >= B[i]:
            have = min(have, A[i] - B[i])
    need = need[0]
    print("YES" if need <= have and have != float('inf') else "NO")