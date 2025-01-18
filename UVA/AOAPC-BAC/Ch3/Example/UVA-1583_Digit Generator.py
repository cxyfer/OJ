"""
    預處理出每個數字的Digit Generator
    tags: 預處理, 紫書-Ch3, CPE-190326
"""
MAX_N = int(1e5 + 5)
ans = [0] * MAX_N

for x in range(1, MAX_N):
    tmp = y = x
    while tmp:
        y += tmp % 10
        tmp //= 10
    if y < MAX_N and ans[y] == 0:
        ans[y] = x
n = int(input())
for _ in range(n):
    x = int(input())
    print(ans[x])
