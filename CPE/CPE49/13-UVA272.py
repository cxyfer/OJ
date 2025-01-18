flag = 0

while (True):
    try:
        line = input()
    except EOFError:
        break

    for ch in line:
        if ch == "\"":
            print("``" if flag == 0 else "''", end="")
            flag = flag ^ 1
        else:
            print(ch, end="")
    print()