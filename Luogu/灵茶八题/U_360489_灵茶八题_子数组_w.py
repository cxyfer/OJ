"""
U360489 灵茶八题 - 子数组 ^w+
https://www.luogu.com.cn/problem/U360489

按位拆分 + 貢獻法
由於 XOR 運算每一位是獨立的，所以可以將數字拆成二進位，單獨考慮每一位對最終答案的貢獻。
如此問題便可以轉換成：給定一個只包含 0 和 1 的陣列，有多少個子陣列的異或和是 1？
這可以用前綴異或和來解決，透過枚舉右端點 s[r]，統計滿足 s[r] ^ s[l] = 1 的左端點 l 的個數。
"""
def solve():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n
    
    ans = 0
    for b in range(22):
        # 求在第 b 位上，有多少個子陣列的異或和為 1
        s = cur = 0
        cnt = [1, 0]
        for x in A:
            s ^= (x >> b) & 1
            cur += cnt[s ^ 1]
            cnt[s] += 1
        ans += cur * (1 << b)
    print(ans)

if __name__ == "__main__":
    solve()