/*
    DP，從可以刪除的數字轉移
*/
#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, tmp, x;
    cin >> n;
    vector<int> dp(n + 1, INF);
    dp[0] = 0;
    for (int i = 1; i <= n; i++) {
        // 枚舉可以刪除的數字
        tmp = i;
        while (tmp > 0) {
            x = tmp % 10;
            tmp /= 10;
            if (x > 0) dp[i] = min(dp[i], dp[i - x] + 1);
        }
    }
    cout << dp[n] << endl;
    return 0;
}