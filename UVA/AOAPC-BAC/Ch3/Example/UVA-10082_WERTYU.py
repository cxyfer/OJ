"""
    字串索引
    tags: string, 紫書-Ch3, CPE-160322
"""
keyboard = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"

while True:
    try:
        line = input()
    except EOFError:
        break
    for ch in line:
        if ch == " ":
            print(" ", end="")
        else:
            print(keyboard[keyboard.index(ch) - 1], end="")
    print()