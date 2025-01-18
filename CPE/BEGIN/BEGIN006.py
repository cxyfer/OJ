while True:
    try:
        line = input()
    except EOFError:
        break
    if not line:
        break
    print("Sum=%d" % sum(list(map(int, line.split()))))