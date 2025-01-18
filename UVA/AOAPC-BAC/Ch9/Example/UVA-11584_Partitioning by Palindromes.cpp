/*
    DP：回文分割
    Python 在 UVA 會 TLE，需要用 C++
    CPE 能過，但測資又双叒叕有不符合格式的情況了，還是暗資，不通靈根本發現不了
    tags: DP, 回文, 紫書, CPE-221213
*/
#include <bits/stdc++.h>
using namespace std;
const int N = 1005;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, dp[N];
    bool is_palindrome[N][N];
    string s;
    cin >> t;
    while (t--) {
        cin >> s;
        int n = s.size();
        memset(is_palindrome, 0, sizeof(is_palindrome));
        for (int i = 0; i < n; i++) is_palindrome[i][i] = true;
        for (int k = 2; k <= n; k++) {
            for (int i = 0; i < n-k+1; i++) {
                int j = i + k - 1;
                if (k == 2) is_palindrome[i][j] = s[i] == s[j];
                else is_palindrome[i][j] = s[i] == s[j] && is_palindrome[i+1][j-1];
            }
        }
        memset(dp, 0, sizeof(dp));
        for (int i = 1; i <= n; i++) {
            dp[i] = i;
            for (int j = 0; j < i; j++) {
                if (is_palindrome[j][i-1]) dp[i] = min(dp[i], dp[j] + 1);
            }
        }
        cout << dp[n] << endl;
    }
    return 0;
}