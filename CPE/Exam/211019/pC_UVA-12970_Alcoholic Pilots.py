"""
    t1 = d1 / v1, t2 = d2 / v2
    t1 + t2 = d1 / v1 + d2 / v2 = (d1 * v2 + d2 * v1) / (v1 * v2)
"""
from math import gcd
kase = 1
while True:
    v1, d1, v2, d2 = map(int, input().split())
    if v1 == 0 and d1 == 0 and v2 == 0 and d2 == 0:
        break
    a = d1 * v2 + d2 * v1
    b = 2 * v1 * v2
    g = gcd(a, b)
    t1, t2 = d1 / v1, d2 / v2
    print(f"Case #{kase}: ", end="")
    print("You owe me a beer!" if d1 * v2 < d2 * v1 else "No beer for the captain.")
    print(f"Avg. arrival time: ", end="")
    print(f"{a // g}" if b // g == 1 else f"{a // g}/{b // g}")
    kase += 1