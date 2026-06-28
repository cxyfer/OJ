"""
P14357 [CSP-J 2025] 拼数 / number
https://www.luogu.com.cn/problem/P14357
"""


def solve():
    s = input().strip()

    cnt = [0] * 10
    for c in s:
        if c.isdigit():
            cnt[ord(c) - ord("0")] += 1

    ans = []
    for i in range(9, -1, -1):
        ans.append(str(i) * cnt[i])
    print("".join(ans))


if __name__ == "__main__":
    solve()
