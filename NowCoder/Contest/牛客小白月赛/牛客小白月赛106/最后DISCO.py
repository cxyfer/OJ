a, b, c, d = map(int, input().split())

# x = pow(a, b, 2) * c + d
if b == 0:
    a = 1
x = a * c + d
print("YES" if x & 1 else "NO")