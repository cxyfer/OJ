"""
分組循環，記錄每組長度。
"""

S = input()
n = len(S)

ans = []
i = 1
while i < n:
    st = i
    while i < n and S[i] != '|':
        i += 1
    ans.append(i - st)
    i += 1
print(*ans)