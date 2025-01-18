from math import *

BASE = 6440
while True:
    try:
        s, a, typ = input().split()
        s, a = int(s), int(a)
    except EOFError:
        break
    if typ == "min":
        a /= 60
    if a > 180:
        a = 360 - a
    radian = a * pi / 180
    arc = (BASE + s) * radian
    chord = (BASE + s) * sin(radian / 2) * 2
    print("{:.6f} {:.6f}".format(arc, chord))