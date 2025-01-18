from math import isqrt # Python 3.8+

while True:
    n = int(input())
    if n == 0:
        break
    print("yes" if int(n ** 0.5) ** 2 == n else "no")