"""
在 2171D 的基礎上，要求構建答案。

基於前一道題目的思路，不難想到可以往前綴最小值連一條邊，但這樣會漏掉先前的前綴最小值。
例如 [2, 3, 1, 4, 5]，則會被分成 [2, 3] 和 [1, 4, 5] 兩個部分，每個連通分量對應一段前綴最小值。
因此對於這種情況，先把未與其他部分連通的最小值保存，之後遇到能連接的點時，再將其連接。

可以用矛盾法證明，當有解時，所有數字都會被連接。
假設有解，令 mn1 為第一個前綴最小值，mn2 為第二個前綴最小值。
如果後續無法連接，代表所有 > mn1 的數字都在 mn2 的左側，
由於 mn2 是 mn1 後第一個 < mn1 的數字，所以 mn2 左側的值都 >= mn1，
這意味著在 mn2 前一個位置會達成無解的情況，與假設矛盾。
"""
from collections import deque

def solve():
    n = int(input())
    P = list(map(int, input().split()))

    dq = deque()
    edges = []
    for i, p in enumerate(P):
        if not dq or p < dq[-1]:
            dq.append(p)
        else:
            edges.append((dq[-1], p))
        if i < n - 1 and dq[-1] == n - i:
            print("No")
            break
        while len(dq) > 1 and p > dq[0]:
            edges.append((dq[0], p))
            dq.popleft()
    else:
        print("Yes")
        for u, v in edges:
            print(u, v)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()