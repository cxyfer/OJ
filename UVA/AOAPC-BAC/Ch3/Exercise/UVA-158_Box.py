while True:
    try:
        data = []
        for _ in range(6):
            w, h = map(int, input().split())
            data.append((w, h) if w < h else (h, w))
    except EOFError:
        break
    flag = True
    data.sort()
    for i in range(0, 6, 2):
        if data[i] != data[i+1]:
            flag = False
            break
    a, b, c = data[0][0], data[0][1], data[2][1]
    if not (a == data[2][0] and b == data[4][0] and c == data[4][1]):
        flag = False
    if flag:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")

