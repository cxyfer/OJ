N, H, X = map(int, input().split(" "))
P = list(map(int, input().split(" ")))

ans = -1
for i, p in enumerate(P):
    if H + p == X:
        ans = i + 1
        break
    elif H + p > X:
        if ans == -1 or p < P[ans]:
            ans = i + 1
print(ans)