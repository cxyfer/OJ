DICT = "qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"

while True:
    try:
        s = input()
    except EOFError:
        break
    for ch in s:
        if ch.lower() in DICT:
            print(DICT[DICT.index(ch.lower()) - 2], end="")
        else:
            print(ch, end="")
    print()