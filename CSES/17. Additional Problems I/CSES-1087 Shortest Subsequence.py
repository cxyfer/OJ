"""
CSES-1087 Shortest Subsequence
https://cses.fi/problemset/task/1087

Greedy
如果 s 可以被劃分成 k 個連續區間，每個區間包含 ALPHA 中的所有字元，
那麼一定能構造出任意長度為 k 的子序列，因此最短的非子序列長度為 k + 1。
基於貪心策略，可以使 k 盡可能的小。只要從左到右遍歷 s，當且僅當遇到最後一種字元時才進行切分即可。
"""
ALPHA = "ACGT"

def solve():
    s = input()

    ans = []
    vis = set()
    for ch in s:
        vis.add(ch)
        if len(vis) == len(ALPHA):
            ans.append(ch)
            vis.clear()
    for ch in ALPHA:
        if ch not in vis:
            ans.append(ch)
            break
    print("".join(ans))

if __name__ == "__main__":
    solve()