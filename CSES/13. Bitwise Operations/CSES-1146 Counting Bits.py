n = int(input())

ans = 0
base = 1
while base <= n:
    q, r = divmod(n + 1, base * 2)
    ans += q * base + max(0, r - base)
    base *= 2

print(ans)