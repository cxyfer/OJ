#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

string s, t;
int m, n;

void solve1() {
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
    for (int i = 0; i <= m; i++) dp[i][n] = m - i;
    for (int j = 0; j <= n; j++) dp[m][j] = n - j;
    for (int i = m - 1; i >= 0; i--) {
        for (int j = n - 1; j >= 0; j--) {
            if (s[i] == t[j]) dp[i][j] = dp[i + 1][j + 1];
            else dp[i][j] = min(dp[i + 1][j], min(dp[i][j + 1], dp[i + 1][j + 1])) + 1;
        }
    }
    cout << dp[0][0] << endl;
}

void solve2() {
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
    for (int i = 1; i <= m; i++) dp[i][0] = i;
    for (int j = 1; j <= n; j++) dp[0][j] = j;
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (s[i - 1] == t[j - 1]) dp[i][j] = dp[i - 1][j - 1];
            else dp[i][j] = min(dp[i - 1][j], min(dp[i][j - 1], dp[i - 1][j - 1])) + 1;
        }
    }
    cout << dp[m][n] << endl;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    cin >> s >> t;
    m = s.size(), n = t.size();

    // solve1();
    solve2();

    return 0;
}