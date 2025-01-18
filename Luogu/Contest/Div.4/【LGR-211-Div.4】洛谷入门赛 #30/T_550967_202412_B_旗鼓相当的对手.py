X1 = list(map(int, input().split()))
X2 = list(map(int, input().split()))

ans = 0
for i, (x1, x2) in enumerate(zip(X1, X2)):
    for j in range(i + 1, 4):
        y1, y2 = X1[j], X2[j]
        if x1 > y1 and x2 < y2 or x1 < y1 and x2 > y2:
            ans += 1

print(ans)