import math

T = int(input())

for tc in range(1, T+1):
    a = int(input(), 2)
    b = int(input(), 2)
    if math.gcd(a, b) == 1:
        print(f"Pair #{tc}: Love is not all you need!")
    else:
        print(f"Pair #{tc}: All you need is love!")