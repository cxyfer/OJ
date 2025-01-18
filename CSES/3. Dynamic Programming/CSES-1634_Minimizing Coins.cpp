#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, x;
    cin >> n >> x;
    vector<int> coins(n);
    for (int i = 0; i < n; i++) cin >> coins[i];
    sort(coins.begin(), coins.end()); // Not necessary, but can be faster
    vector<int> dp(x + 1, INF);
    dp[0] = 0;
    for (int i = 0; i < n; i++) {
        for (int j = coins[i]; j <= x; j++) {
            dp[j] = min(dp[j], dp[j - coins[i]] + 1);
        }
    }
    cout << (dp[x] != INF ? dp[x] : -1) << endl;
    return 0;
}