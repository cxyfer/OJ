while True:
    try:
        n = int(input())
    except:
        break
    if n == 0:
        break
    dices = [1, 6, 2, 5, 3, 4] # 上下北南西東
    for _ in range(n):
        cmd = input()
        if cmd == "north":
            dices = [dices[3], dices[2], dices[0], dices[1], dices[4], dices[5]]
        elif cmd == "south":
            dices = [dices[2], dices[3], dices[1], dices[0], dices[4], dices[5]]
        elif cmd == "east":
            dices = [dices[4], dices[5], dices[2], dices[3], dices[1], dices[0]]
        elif cmd == "west":
            dices = [dices[5], dices[4], dices[2], dices[3], dices[0], dices[1]]
    print(dices[0])