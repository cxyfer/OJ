"""
L - 变鸡器
https://ac.nowcoder.com/acm/contest/95338/L

保留一組 CHICKEN，其他全部刪除。
由於刪除時只能刪除不同的兩個字元，故剩餘字元數量必須為偶數；
且不能有任何一個字元數量超過剩餘字元數量的一半。
"""
from collections import Counter

tgt = "CHICKEN"

def solve():
    n = int(input())
    s = input()
    assert len(s) == n

    # 剩餘字元數量為奇數，無法兩兩刪除
    if (n - 7) & 1:  
        print("NO")
        return
    
    cnt = Counter(s)
    for ch in tgt:
        cnt[ch] -= 1

    # 有某個字元數量超過剩餘字元數量的一半，無法兩兩刪除
    if any(cnt[ch] < 0 for ch in tgt) or any(v > (n - 7) // 2 for v in cnt.values()):
        print("NO")
        return

    # 檢查是否能保留一組 CHICKEN
    idx = 0
    for ch in s:
        if ch == tgt[idx]:
            idx += 1
            if idx == len(tgt):
                print("YES")
                return
    print("NO")

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
