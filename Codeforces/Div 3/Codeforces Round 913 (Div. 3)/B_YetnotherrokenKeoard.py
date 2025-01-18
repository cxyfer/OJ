from collections import deque

T = int(input())

for tc in range(1, T+1):
    S = input()
    lower = []
    upper = []

    n = len(S)
    ans = list(S)


    for idx, ch in enumerate(S):
        if ch == 'b':
            ans[idx] = ""
            if lower:
                ans[lower.pop()] = ""
                
        elif ch == 'B':
            ans[idx] = ""
            if upper:
                ans[upper.pop()] = ""
        elif ch.islower():
            lower.append(idx)
        else:
            upper.append(idx)
    print("".join(ans))