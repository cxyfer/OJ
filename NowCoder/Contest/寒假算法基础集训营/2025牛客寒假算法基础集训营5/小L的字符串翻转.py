"""
D - 小L的字符串翻转
https://ac.nowcoder.com/acm/contest/95337/D

1. 前綴和 + 調和級數貢獻

在每個劃分出的01段中，可能存在一種數字或兩種數字：
- 如果只有一種數字，可以透過翻轉來與前一段最後的數字 c 相同，對答案無貢獻
- 如果有兩種數字，可以透過重新排列將 c 排在這一段前面，後面是 1 ^ c，對答案有 1 的貢獻

預處理前綴和，可以在 O(1) 的時間內得到區間內 0 和 1 的數量。
由於段落數為 n + n / 2 + n / 3 + ... + n / n，根據調和級數，時間複雜度為 O(n log n)。

2. 貢獻

基於上述討論，轉換為以下的貢獻方式：
- 若每一個 01 段皆有兩種數字，則 ans[k] 的初始值為 ceil(n / k) + 1
- 若有某個 01 段只有一種數字，則對答案的貢獻為 -1

若某一個 01 段對答案有 -1 的貢獻，則這一個 01 段，一定在某段連續的相同數字中，將其稱作 seg
故轉換為考慮所有的 seg，計算其對答案的貢獻。

對於長度為 ln 的 seg，可以對 ans[1], ans[2], ..., ans[ln] 造成貢獻。
但最後一個 seg 可以對所有的 ans[1], ans[2], ..., ans[n] 造成貢獻。

計算貢獻時只需要考慮這一個 seg 可以涵蓋多少個01段即可，為此需要將左端點對齊到某 01 段的開頭。
可以得到其對 ans[k] 的貢獻為 floor(ln / k)。
注意最後一個 seg 可以再多計入不完整的最後一段，即 ceil(ln / k)。
"""
from functools import reduce

def solve1():
    n = int(input())
    s = input()
    assert len(s) == n

    s0 = [0] * (n + 1)
    s1 = [0] * (n + 1)
    for i, c in enumerate(s, 1):
        s0[i] = s0[i - 1] + (c == '0')
        s1[i] = s1[i - 1] + (c == '1')

    ans = 0
    for k in range(1, n + 1):
        cur = (n + k - 1) // k + 1  # ceil(n / k) + 1
        for i in range(1, n + 1, k):
            cnt0 = s0[min(n, i + k - 1)] - s0[i - 1]
            cnt1 = s1[min(n, i + k - 1)] - s1[i - 1]
            if cnt0 == 0 or cnt1 == 0:
                cur -= 1
        ans ^= cur
    print(ans)

def solve2():
    n = int(input())
    s = input()
    assert len(s) == n

    segs = []
    i = 0
    while i < n:
        j = i
        while j + 1 < n and s[j + 1] == s[i]:
            j += 1
        segs.append((i, j))
        i = j + 1
    
    ans = [0] * (n + 1)
    for k in range(1, n + 1):
        ans[k] = (n + k - 1) // k + 1

    for l, r in segs:
        # 除了最後一個 seg 外，每一各 seg 只會對 ans[1], ans[2], ..., ans[ln] 造成貢獻
        ln = r - l + 1
        for k in range(1, (ln if r < n - 1 else n) + 1):
            ll = (l + (k - 1)) // k * k  # 對齊到某個 01 段的開頭
            if r < n - 1:  # 這一個 seg 涵蓋的完整 01 段數，即 floor(ln / k)
                ans[k] -= (r - ll + 1) // k
            else:  # 最後一個 seg 可以再多計入不完整的最後一段，即 ceil(ln / k)
                ans[k] -= (r - ll + 1 + k - 1) // k
    print(reduce(lambda x, y: x ^ y, ans))

# solve = solve1
solve = solve2
if __name__ == "__main__":
    solve()