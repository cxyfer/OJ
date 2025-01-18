from math import sqrt

t = int(input())

def dis(x1, y1, x2, y2):
    return sqrt((x1-x2)**2+(y1-y2)**2)

for tc in range(t):
    Px, Py = map(int, input().split())
    Ax, Ay = map(int, input().split())
    Bx, By = map(int, input().split())
    PA = dis(Px, Py, Ax, Ay)
    PB = dis(Px, Py, Bx, By)
    AB = dis(Ax, Ay, Bx, By)
    OP = dis(0, 0, Px, Py)
    OA = dis(0, 0, Ax, Ay)
    OB = dis(0, 0, Bx, By)
    # case 1: 若 O,P 皆在同一個圓內
    RA = max(PA, OA) # 若皆在以 A 為圓心的圓內
    RB = max(PB, OB) # 若皆在以 B 為圓心的圓內  
    # case 2: 若 O,P 分別在兩個圓內
    d = AB / 2 # 相切
    # case 2a: O 在 A，P 在 B
    R3 = max(OA, AB/2, PB)
    # case 2b: O 在 B，P 在 A
    R4 = max(OB, d, PA)
    print("{:.10f}".format(min(RA, RB, R3, R4)))