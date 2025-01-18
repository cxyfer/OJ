N, Q = map(int, input().split())
S = input()
queries = [list(map(int, input().split())) for _ in range(Q)]

DIR = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}

for x, y, l, r in queries:
    if (x, y) == (0, 0):
        print("YES")
        continue
    SS = S[:l-1] + S[l-1:r][::-1] + S[r:]
    st = (0, 0)
    flag = False
    for c in SS:
        st = (st[0] + DIR[c][0], st[1] + DIR[c][1])
        if st == (x, y):
            flag = True
            break
    print("YES" if flag else "NO")
    
