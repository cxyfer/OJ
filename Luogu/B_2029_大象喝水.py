import math
h, r = map(int, input().split())
print(math.ceil(20 * 1e3/ (r * r * 3.14 * h)))