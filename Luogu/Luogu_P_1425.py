a, b, c, d = map(int, input().split())
h, m = (c - a),  d - b
if m < 0:
    h -= 1
    m += 60
print(h, m)