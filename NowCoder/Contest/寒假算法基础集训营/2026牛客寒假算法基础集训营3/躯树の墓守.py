"""
E. 躯树の墓守
https://ac.nowcoder.com/acm/contest/120563/E

構造
以星狀圖的作為 MST 的樹邊，中心點為 1，其他點為 2, 3, ..., n。
對於冗餘的非樹邊，可以從已經連通的點中，選擇兩個尚未連接的節點，並將其連接。

那麼我們可以選定一組權重 W = (W1, W2, ..., W(n-1))，連接中心點與其他點，使得權重和為 k。
但對於第 i 條樹邊 Wi，存在限制：在其以前（包含本身）最多有
- i 條樹邊
- C(i - 1, 2) = (i - 1) * (i - 2) / 2 條非樹邊
因此 Wi 的上限為 i + (i - 1) * (i - 2) / 2。
又為了不破壞上述結構上的性質，可以使 W 保持有序，即 Wi 的值需要 < W(i+1)。

將 W 初始化為 [1, 2, ..., n-1]，並從最大的邊開始嘗試增加，直到權重和為 k 為止。
"""
def solve():
    n, m, k = map(int, input().split())

    # 1. 初始權重設為最小可能值 [1, 2, ..., n-1]
    W = list(range(1, n))
    s = sum(W)

    if k < s:
        print("NO")
        return

    # 2. 貪心調整權重：從最大的邊開始嘗試增加
    for i in range(n - 2, -1, -1):
        # 計算 W[i] 的理論上限
        limit1 = (i + 1) + i * (i - 1) // 2
        limit2 = W[i+1] - 1 if i < n - 2 else m
        L = min(limit1, limit2)

        # 計算可增加的空間
        if L - W[i] > 0:
            add = min(k - s, L - W[i])
            W[i] += add
            s += add
        
        if s == k:
            break
    
    if s != k:
        print("NO")
        return

    # 3. 構造圖形
    v = 2
    x, y = 2, 3
    st = set(W)
    ans = []
    
    # 遍歷所有邊權 1 到 m
    for w in range(1, m + 1):
        if w in st:
            # 分配給樹邊 (1, v)
            ans.append((1, v, w))
            v += 1
        else:
            # 分配給非樹邊 (x, y)
            ans.append((x, y, w))
            # 更新 x, y 以生成下一個邊 (2,3) -> (2,4) -> (3,4) -> (2,5)...
            x += 1
            if x == y:
                y += 1
                x = 2

    print("YES")
    for u, v, w in ans:
        print(u, v, w)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()