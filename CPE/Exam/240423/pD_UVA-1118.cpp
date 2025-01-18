// """
//     雖然 CPE 上的這題可以很暴力過，但是在 UVA 上這題是數學題
//     UVA 上的測資會讓遞迴深度會超過限制，就算開了遞迴限制也會 TLE 。
//     UVA 上 m, n 的範圍最大到 1000000000，這個範圍的遞迴會爆炸。

//     S(n, m) represents the number of ways to partition a set of n
// things into m nonempty subsets.
//     S(n, m) 表示 n 個物品分成 m 個**非空子集**的方法數，
//     即將 n 個相異物放置到 m 個相異箱子中，每個箱子至少有一個物品的方法數。
//     題目很貼心的給了遞迴式，但是也可以用組合證法推導出來：固定一物 x 
//         - 若 x 獨立一組，則剩下 n-1 個物品分成 m-1 個非空子集，有 S(n-1, m-1) 種方法。
//         - 若 x 與其他物品一起放置，則剩下 n-1 個物品分成 m 個非空子集，有 m*S(n-1, m) 種方法。
//     得 S(n, m) = S(n-1, m-1) + m*S(n-1, m)
//     再來考慮邊界條件：
//     - 當 n = m 或 m = 1 時，只有一種方法，即S(n, m) = 1
//     - 當 n < m 時，不存在非空子集，即S(n, m) = 0
//     寫成遞迴式後，畫龍點睛加上 @cache 進行記憶化搜索，避免重複計算。
// """
// from functools import cache
// import sys
// buf = sys.stdin.read().split()
// def cin(): return buf.pop(0)
// sys.setrecursionlimit(2147483617)

// @cache # Memoization
// def S(n, m):
//     if n < m or m == 0: # 箱子比物品多，存在空集合：或是箱子數為 0，不存在非空子集
//         return 0
//     if n == m:
//         return 1
//     if n == 0:
//         return 1 if m == 0 else 0


//     return (S(n-1, m-1) + m * S(n-1, m)) &1

// # t = int(input())
// t = int(cin())
// for _ in range(t):
//     n, m = map(int, [cin(), cin()])
//     print(S(n, m) & 1)

#include <bits/stdc++.h>
using namespace std;
const int N = 1005;
#define endl '\n'

int dp[N][N];

int S(int n, int m) {
    if (n < m || m == 0) return 0;
    if (n == m) return 1;
    if (n == 0) return m == 0 ? 1 : 0;
    if (dp[n][m] != -1) {
        return dp[n][m];
    }
    return dp[n][m] = (S(n-1, m-1) + m * S(n-1, m)) & 1;
}
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, n, m;
    cin >> t;
    memset(dp, -1, sizeof(dp));
    while (t--) {
        cin >> n >> m;
        cout << (S(n, m) & 1) << endl;
    }
    return 0;
}