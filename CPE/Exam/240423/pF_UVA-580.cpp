#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int N = 35;
#define endl '\n'

LL comb(int n, int k) {
    LL numerator = 1, denominator = 1;
    for (int i = 0; i < k; i++) {
        numerator *= n-i;
        if (numerator % (k-i) == 0) {
            numerator /= k-i;
        } else {
            denominator *= k-i;
        }
    }
    return numerator / denominator;
}

void solve1() { // 1. Math
    int n;
    while (cin >> n && n) {
        LL legal = 0;
        for (LL u1 = 0; u1 <= n; u1++) {
            for (LL u2 = 0; u2 <= n/2; u2++) {
                LL k = n - u1 - 2*u2;
                if (k + 1 < u1 + u2){
                    break;
                }
                LL c1 = comb(k+1, u1+u2);
                LL c2 = comb(u1+u2, u1);
                legal += c1 * c2; 
            }
        }
        LL ans = 1 << n;
        ans -= legal;
        cout << ans << endl;
    }
}

void solve2() { // 2. DP
    int n;
    LL dp[N][3] = {0}; // dp[i][j] 表示長度為 i 的字串，後綴中有連續 j 個 U 的情況數
    dp[0][0] = 1;
    for (int i = 1; i < N; i++) {
        dp[i][0] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2];
        dp[i][1] = dp[i-1][0];
        dp[i][2] = dp[i-1][1];
    }
    while (cin >> n && n) {
        cout << (1 << n) - dp[n][0] - dp[n][1] - dp[n][2] << endl;
    }
}
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    // solve1();
    solve2();
    return 0;
}