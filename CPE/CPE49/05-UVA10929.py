while True:
    s = input()
    if s == "0":
        break
    
    s_odd = s_even = 0
    for i, ch in enumerate(s):
        if i & 1:
            s_odd += int(ch)
        else:
            s_even += int(ch)
    if (s_even - s_odd) % 11 == 0:
        print(f"{s} is a multiple of 11.")
    else:
        print(f"{s} is not a multiple of 11.")