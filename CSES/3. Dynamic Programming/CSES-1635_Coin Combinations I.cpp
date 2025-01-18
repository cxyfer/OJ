#include <bits/stdc++.h>
using namespace std;
const int MOD = 1e9 + 7;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, x;
    cin >> n >> x;
    vector<int> coins(n);
    for (int i = 0; i < n; i++) cin >> coins[i];
    sort(coins.begin(), coins.end());
    vector<int> dp(x + 1, 0);
    dp[0] = 1;
    // 刷表法
    // for (int i = 0; i <= x; i++) {
    //     for (int c : coins) {
    //         if (i + c > x) break;
    //         dp[i + c] += dp[i];
    //         dp[i + c] %= MOD;
    //     }
    // }
    // 填表法
    for (int i = 0; i <= x; i++) {
        for (int c : coins) {
            if (i - c < 0) break;
            dp[i] += dp[i - c];
            dp[i] %= MOD;
        }
    }
    cout << dp[x] << endl;
    return 0;
}