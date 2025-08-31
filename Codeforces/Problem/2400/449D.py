"""
CF449D Jzzhu and Numbers
https://codeforces.com/problemset/problem/449/D
SOS DP + 排容原理

令 ans(S) 為 AND 結果恰好為 S 的子集數量。我們要求的目標是 ans(0)，但這很難計算，可以把考慮把這種恰好的問題轉換為至少的問題。

令 N(S) 為 AND 結果至少 是 S ，也就是結果是 S 的超集的子集數量，對於一個子集，其 AND 結果為 R，如果 R & S = S，那麼這個子集就被計入 N(S)。

N(S) = sum_{T in S} ans(T)，可以由子集反演或排容原理來得到 ans(S) 的表達式：ans(S) = sum_{S in T} (-1)^{|T| - |S|} N(T)。

而 N(S) 可以透過在輸入陣列 A 中，找到有多少個數是 S 的超集來計算，令這個數量為 C(S)，則 N(S) 即為在其中任選一個非空子集的方案數 2^(C(S)) - 1。
而 S 的超集中的元素數量 C(S)，也就是滿足 (S & y) == S 的 y 個數，可以透過 SOS DP 來計算。
"""
MOD = int(1e9 + 7)

def solve():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n
    B = max(A).bit_length()
    U = 1 << B

    f = [0] * U
    for x in A:
        f[x] += 1
    
    for i in range(B):
        for s in range(U - 1, -1, -1):
            if (s >> i) & 1:
                f[s ^ (1 << i)] += f[s]
 
    ans = 0
    for i in range(U):
        term = pow(2, f[i], MOD) - 1
        ans += -term if i.bit_count() & 1 else term
        ans %= MOD
    print(ans)

if __name__ == '__main__':
    solve()