"""
g = x * b + y * (a % b)
  = x * b + y * (a - floor(a / b) * b)
  = y * a + (x - y * floor(a / b)) * b
"""
def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = egcd(b, a % b)
    return g, y, x - a // b * y

while True:
    try:
        a, b = map(int, input().split())
    except EOFError:
        break
    g, x, y = egcd(a, b)
    print(x, y, g)