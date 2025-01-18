from collections import Counter
t = int(input())
for case in range(t):
    # print("Case #{}: ".format(case+1))
    n = int(input())
    matrix = [list(input()) for _ in range(n)]
    # print(matrix)
    ans = 0
    for i in range(n//2):
        for j in range(n//2):
            p1 = (i, j)
            p2 = (j, n-1-i)
            p3 = (n-1-i, n-1-j)
            p4 = (n-1-j, i)
            targets = [ matrix[p[0]][p[1]] for p in [p1, p2, p3, p4] ]
            ords = list(map(ord, targets))
            max_ord = max(ords)
            ans += sum([ max_ord - ord_i for ord_i in ords ])
    print(ans)