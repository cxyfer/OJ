N, L, R = map(int, input().split())
A = list(map(int, input().split()))

ans = [0] * N

for i, a in enumerate(A):
    if L <= a <= R:
        ans[i] = a
    elif a < L:
        ans[i] = L
    else:
        ans[i] = R
print(*ans)