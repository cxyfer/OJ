"""
J. Branch of Faith
https://ac.nowcoder.com/acm/contest/120563/J

Complete Binary Tree 每層的節點數量（若全滿）為：
- 第 0 層：1 個
- 第 1 層：2 個
- 第 2 層：4 個
- 第 3 層：8 個
- ...
- 第 d 層：2^d 個
故第 d 層的節點編號為 [2^d, 2^(d+1)-1]，且 x 屬於第 log2(x) 層。
然而第 d 層可能不全滿，因此需要對總數量取 min。
"""
def solve():
    n, q = map(int, input().split())
    
    for _ in range(q):
        x = int(input())

        d = x.bit_length() - 1
        st = 1 << d
        ed = min((1 << (d + 1)) - 1, n)
        print(ed - st + 1)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()