t = int(input())

for _ in range(t):
    n = int(input())
    fa = [-1] + [int(x)-1 for x in input().split()]
    S = input()

    dp1, dp2 = [0] * (n+1), [0] * (n+1)
    
    for i in range(n-1, -1, -1):
        if S[i] == "S":
            dp1[i] = float("inf")
        elif S[i] == "P":
            dp2[i] = float("inf")

        p = fa[i]
        if p != -1:
            dp1[p] += min(dp1[i], dp2[i]+1)
            dp2[p] += min(dp1[i]+1, dp2[i])
        
    print(min(dp1[0], dp2[0]))