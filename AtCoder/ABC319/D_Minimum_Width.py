N, M = map(int, input().split(" "))
L = list(map(int, input().split(" ")))

if M == 1:
    print(sum(L) + (N-1))
    exit()

"""
    Binary Search for lenght of a line: l ~ r
"""

l = max(L) - 1
r = sum(L) + N
while l + 1 < r:
    mid = (l+r) // 2
    line = 1 # number of lines
    cur = -1 # current length of a line
    for li in L:
        cur += li + 1
        if cur > mid:
            line += 1
            cur = li
    if line <= M: # if line <= M, then we can make it shorter
        r = mid
    else:
        l = mid
print(r)
exit()

ideal = sum(L) // M +1
def check(target=ideal, L=L.copy()):
    for i in range(M):
        if i >= len(L):
            return False, L
        while (L[i] < ideal):
            b = L.pop(i+1)
            L[i] += b + 1
    return True, L
def check2(boundary, L=L.copy()):
    for i in range(M):
        if i >= len(L):
            return False, L
        while (L[i] < boundary):
            if i+1 >= len(L):
                break
            if L[i] + L[i+1] + 1 > boundary:
                break
            b = L.pop(i+1)
            L[i] += b + 1
    return (True, L) if len(L) == M else (False, L)
ret, ans = check(ideal, L.copy())
if ret:
    print(max(ans))
    exit()
else:
    finalAns = []
    for bound in ans:
        res, ans = check2(bound, L.copy())
        # print(len(ans), ans)
        if res:
            finalAns.append(max(ans))
    print(min(finalAns))
        