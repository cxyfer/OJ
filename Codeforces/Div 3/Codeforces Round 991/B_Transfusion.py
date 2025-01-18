t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    o = e = 0
    for i, x in enumerate(A):
        if i & 1:
            o += x
        else:
            e += x
    cnt_o = n // 2
    cnt_e = (n + 1) // 2
    if (o % cnt_o) == 0 and (e % cnt_e) == 0 and (o // cnt_o) == (e // cnt_e):
        print("YES")
    else:
        print("NO")