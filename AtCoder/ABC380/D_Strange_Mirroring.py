"""
令 0 表示未翻轉，1 表示翻轉

對於範例 aB 而言，前四次操作如下：
00
0011
00111100
0011110011000011

對於 k = 15 而言，他上次是由 k = 7 翻轉而來；再上次是 k = 3，再再上次是 k = 1，這已經在原始字串中，因此不再翻轉。
故 k = 15 相對 k = 1 翻轉了 3 次。

故可以維護長度 [n, 2n, 4n, 8n, 16n, ...]，由後往前檢查翻轉次數，若翻轉次數為奇數則翻轉，否則不翻轉。
由於確保 k <= 1e18，因此長度最多到 1e18 即可。
"""

S = input()
Q = int(input())
queries = list(map(int, input().split()))

n = len(S)
ln = [n]
MAX_LN = 1e18
while ln[-1] <= MAX_LN:
    ln.append(ln[-1] * 2)
m = len(ln)

ans = []
for k in queries:
    cnt = 0
    for i in range(m - 1, 0, -1):
        if k > ln[i - 1]:
            k = k - ln[i - 1]
            cnt += 1
    ch = S[k - 1]
    if cnt & 1:
        ch = ch.upper() if ch.islower() else ch.lower()
    ans.append(ch)
print(*ans)