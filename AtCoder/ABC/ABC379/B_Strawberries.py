"""
    分組循環，找到每組 O 的數量 x，該組貢獻為 floor(x / k)
"""
n, k = map(int, input().split())
s = list(input())

ans = 0
i = 0
while i < n:
    j = i
    while j < n and s[j] == 'O':
        j += 1
    ans += (j - i) // k # 此時 [i, j - 1] 皆為 O
    i = j + 1
print(ans)