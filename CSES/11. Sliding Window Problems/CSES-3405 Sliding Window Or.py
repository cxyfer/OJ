n, k = map(int, input().split())
x, a, b, c = map(int, input().split())

A = [x] + [0] * (n - 1)
for i in range(1, n):
    A[i] = (a * A[i - 1] + b) % c

suf = [0] * n
for i in range(n - 1, -1, -1):
    if i == n - 1 or (i + 1) % k == 0:
        suf[i] = A[i]
    else:
        suf[i] = A[i] | suf[i + 1]

ans = pre = 0
for i, x in enumerate(A):
    if i % k == 0:
        pre = x
    else:
        pre |= x
    if i >= k - 1:
        ans ^= (pre | suf[i - k + 1])
print(ans)