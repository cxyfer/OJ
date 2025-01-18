/*
    Longest Palindrome Subsequence
    1. 轉換為 LCS 問題
    2. 區間 DP (Bottom-Up) 枚舉長度，由小區間到大區間
*/
#include <bits/stdc++.h>
using namespace std;
const int N = 1024;
#define endl '\n'

string s, t;
int dp[N][N];

void solve1() {
    int n = s.size();
    string t = s;
    reverse(t.begin(), t.end());
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) {
            if (s[i - 1] == t[j - 1]) dp[i][j] = dp[i - 1][j - 1] + 1;
            else dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
        }
    }
    cout << dp[n][n] << endl;
}

void solve2() {
    int n = s.size();
    if (n == 0) {
        cout << 0 << endl;
        return;
    }
    for (int i = 0; i < n; ++i) dp[i][i] = 1;
    for (int ln = 2; ln <= n; ++ln) {
        for (int i = 0; i <= n - ln; ++i) {
            int j = i + ln - 1;
            if (s[i] == s[j]) dp[i][j] = dp[i + 1][j - 1] + 2;
            else dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
        }
    }
    cout << dp[0][n - 1] << endl;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int T;
    cin >> T;
    cin.ignore();
    while (T--) {
        getline(cin, s);
        memset(dp, 0, sizeof(dp));
        solve1();
        // solve2();
    }
    return 0;
}