#include <bits/stdc++.h>
using namespace std;
const int MOD = 1e9 + 7;
#define endl '\n'

/*
    DP 
    改成先枚舉硬幣，再枚舉金額，就能使同種硬幣先被處理，進而確保不重複。
    
    例如當 coins = [2, 5]，x = 9 時，先枚舉硬幣再枚舉金額會是：
    - 2
    - 2 + 2
    - 2 + 2 + 2
    - 2 + 2 + 2 + 2
    - 5
    - 2 + 5
    - 2 + 2 + 5 (o)
    但先枚舉金額再枚舉硬幣會是：
    - 2
    - 2 + 2
    - 5
    - 2 + 2 + 2
    - 5 + 2
    - 2 + 5
    - 2 + 2 + 2 + 2
    - 5 + 2 + 2 (o)
    - 2 + 5 + 2 (o)
    - 2 + 2 + 5 (o)
*/

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, x;
    cin >> n >> x;
    vector<int> coins(n);
    for (int i = 0; i < n; i++) cin >> coins[i];
    vector<int> dp(x + 1, 0);
    dp[0] = 1;
    for (int c : coins) {
        for (int i = c; i <= x; i++) {
            dp[i] += dp[i - c];
            dp[i] %= MOD;
        }
    }
    cout << dp[x] << endl;
    return 0;
}