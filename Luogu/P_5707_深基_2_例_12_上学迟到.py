import math

s, v = map(int, input().split())

t = (8 * 60 - 10 - math.ceil(s / v)) % (24 * 60)
h, m = divmod(t, 60)
print(f"{h:02d}:{m:02d}")