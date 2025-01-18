"""
差分 + 貢獻 + 模擬進位

考慮第 idx 位數字 d 的貢獻
"""
N = int(input())
S = input()

ans = [0] * (2 * N + 1)
for i, ch in enumerate(S, 1):
    d = ord(ch) - ord('0')
    if d != 0:
        ans[0] += d * i
        ans[N - i + 1] -= d * i

for i in range(1, 2 * N + 1):
    ans[i] += ans[i - 1]

for i in range(2 * N):
    if ans[i] >= 10:
        ans[i + 1] += ans[i] // 10
        ans[i] %= 10

print("".join(map(str, ans[::-1])).lstrip('0'))