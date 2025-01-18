/*
    Dynamic Programming
    dp[i] 表示和為i的完全平方數的最小個數
*/
#include <bits/stdc++.h>
using namespace std;
const int N = 1e4 + 5;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    vector<int> dp(N);
    for (int i = 1; i < N; ++i) {
        dp[i] = i;
        for (int j = 1; j * j <= i; ++j) {
            dp[i] = min(dp[i], dp[i - j * j] + 1);
        }
    }
    int t, n;
    cin >> t;
    while (t--) {
        cin >> n;
        cout << dp[n] << endl;
    }
    return 0;
}