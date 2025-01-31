from math import gcd, hypot

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

H, W = 233333 * 2, 343720 * 2
dx, dy = 15, 17
t = dt = lcm(dx, W) // dx
while True:
    if (t * dy) % H == 0:
        ans = hypot(t * dx, t * dy)
        break
    t += dt
print(f"{ans:.2f}")