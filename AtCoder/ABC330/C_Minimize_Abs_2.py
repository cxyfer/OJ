from math import *

D = int(input())

ans = D # x = y = 0

# minimum value of abs(x**2 + y**2 - D)


for x in range(1, int(D**0.5) + 10):
    if D - x**2 < 0:
        y = 0
        ans = min(ans, abs(x**2 + y**2 - D))
    elif D - x**2 == 0:
        ans = 0
    else:
        y1 = int((D - x**2)**0.5)
        y2 = y1 + 1
        ans = min(ans, abs(x**2 + y1**2 - D))
        ans = min(ans, abs(x**2 + y2**2 - D))
    if ans == 0:
        break

print(ans)