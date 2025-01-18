from collections import Counter

tc = 0
while True:
    try:
        line = input()
        if tc > 0:
            print()
        tc += 1
    except EOFError:
        break
    cnt = Counter(line)
    for k, v in sorted(cnt.items(), key=lambda x: (x[1], -ord(x[0])) ):
        print(ord(k), v)
