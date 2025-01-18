N = 101
mp = [["" for i in range(N)] for j in range(N)]

# read input
r, c = 0, 0
while True:
    try:
        line = input()
    except EOFError:
        break
    n = len(line)
    c = max(c, n) # update matrix width
    for i in range(n):
        mp[r][i] = line[i]
    for i in range(n, c): # fill the rest of the row with space
        mp[r][i] = " "
    r += 1

# output
for i in range(c):
    for j in range(r):
        print(mp[r-1-j][i], end="")
    print()