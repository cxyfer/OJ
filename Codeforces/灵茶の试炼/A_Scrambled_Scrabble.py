from collections import Counter

S = input()
cnt = Counter(S)

tot = len(S)
vowels = sum(cnt[ch] for ch in "AEIOU")
consonants = tot - vowels - cnt["Y"]

ans = 0
# 枚舉 Y 作為子音的數量，令剩下的作為母音
for y_v in range(cnt["Y"] + 1):
    y_c = cnt["Y"] - y_v

    v = vowels + y_v
    c = consonants + y_c

    if v < 1 or c < 2:
        continue

    g = min(v, c // 2)
    extra = min(g * 2, cnt["N"], cnt["G"], c - g * 2)
    ans = max(ans, g * 3 + extra)

print(ans)