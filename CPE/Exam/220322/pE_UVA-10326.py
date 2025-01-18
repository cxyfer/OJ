""" UVA-10326 The Polynomial Equation
    給多項式的根，求多項式。
    模擬多項式乘法過程即可。
"""
while True:
    try:
        n = int(input())
        roots = [] if n == 0 else list(map(int, input().split()))
    except EOFError:
        break
    res = [1]
    for a in roots:
        tmp = [1]
        for j, b in enumerate(res):
            if j < len(res)-1:
                tmp.append(-a*b + res[j+1]) # * (x^1 - a)
            else:
                tmp.append(-a*b)
        res = tmp
    exp = len(res) - 1
    for i, x in enumerate(res):
        m = exp - i # mantissa
        if i == 0:
            if x < 0:
                print("-", end = "")
        else:
            if x == 0 and m > 0:
                continue
            print(" + " if x >= 0 else " - ", end = "")
        x = abs(x)
        if x != 1 or m == 0:
            print(x, end = "")
        if m > 1:
            print(f"x^{m}", end = "")
        elif m == 1:
            print("x", end = "")
    print(" = 0")
