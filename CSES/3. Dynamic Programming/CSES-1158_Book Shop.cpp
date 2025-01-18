#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, x;
    cin >> n >> x;
    vector<int> prices(n), pages(n);
    for (int i = 0; i < n; i++) cin >> prices[i];
    for (int i = 0; i < n; i++) cin >> pages[i];
    // dp[i] 表示花費價格為 i 時的所能獲得的最大頁數
    vector<int> dp(x + 1, 0);
    for (int i = 0; i < n; i++) { // 枚舉每本書
        for (int j = x; j >= prices[i]; j--) { // 枚舉轉移來源
            dp[j] = max(dp[j], dp[j - prices[i]] + pages[i]);
        }
    }
    cout << dp[x] << endl;
    return 0;
}