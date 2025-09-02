S = input()


def cal(s):
    return (s.count('t') - 2) / (len(s) - 2) 
    
n = len(S)
ans = 0
for i, c in enumerate(S):
    if c != 't':
        continue
    for j in range(i + 2, n):
        if S[j] != 't':
            continue
        ans = max(ans, cal(S[i:j + 1]))
print(ans)