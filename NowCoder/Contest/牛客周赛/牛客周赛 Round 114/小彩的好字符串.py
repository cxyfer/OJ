"""
B-小彩的好字符串
https://ac.nowcoder.com/acm/contest/119273/B

雖然這題的範圍允許 O(n^2) 的解法，但上週隔壁的 Weekly Contest 471 有類似的題目：
3714. Longest Balanced Substring II
透過式子變形 + 枚舉右維護左，可以做到 O(n) 的解法
"""

from collections import defaultdict

def solve():
    n = int(input())
    s = input().strip()
    assert n == len(s)

    ans = 0
    mp = defaultdict(int)
    mp[(0, 0)] = 1
    cnt = [0] * 3
    for ch in s:
        cnt[ord(ch) - ord('1')] += 1
        p = (cnt[0] - cnt[1], cnt[1] - cnt[2])
        ans += mp[p]
        mp[p] += 1
    print(ans)

if __name__ == "__main__":
    solve()