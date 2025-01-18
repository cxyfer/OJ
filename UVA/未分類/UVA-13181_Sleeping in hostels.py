import sys
input = lambda: sys.stdin.readline().strip()
print = lambda val: sys.stdout.write(str(val) + "\n")

while True:
    try:
        s = input().strip()
    except:
        break
    if not s:
        break
    n = len(s)
    groups = []
    i = 0
    while i < n:
        while i < n and s[i] == 'X':
            i += 1
        st = i
        while i < n and s[i] == '.':
            i += 1
        groups.append(i - st)
        i += 1
    # print(groups)
    ans = 0
    for g in groups:
        ans = max(ans, (g - 1) // 2)
    if s[0] == '.':
        ans = max(ans, groups[0] - 1)
    if s[-1] == '.':
        ans = max(ans, groups[-1] - 1)
    print(ans)