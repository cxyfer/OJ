"""
1. f(s1, s2)
    st = 0
        2112112112
        2212112
    st = 1, j = 7
        2112112112
         2212112

2. f(s2, s1)
    st = 0
        2212112
        2112112112
    st = 1
        2212112
         2112112112
    st = 2, j = 5
        2212112
          2112112112 

"""
def f(s1, s2): # 固定 s1，移動 s2
    n1, n2 = len(s1), len(s2)
    st = 0
    j = 0
    while (st + j) < n1 and j < n2:
        if not (s1[st + j] == '2' and s2[j] == '2'):
            j += 1
        else:
            st += 1
            j = 0
    return n1 + n2 - j
while True:
    try:
        s1 = input()
        s2 = input()
    except EOFError:
        break
    n1, n2 = len(s1), len(s2)
    ans = min(f(s1, s2), f(s2, s1))
    print(ans)
