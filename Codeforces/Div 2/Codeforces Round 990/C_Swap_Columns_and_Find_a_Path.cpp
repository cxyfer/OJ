#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const LL INF = 0x3f3f3f3f3f3f3f3f;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, n, a, b;
    cin >> t;
    while (t--) {
        cin >> n;
        vector<vector<int>> grid(2, vector<int>(n));
        for (int i = 0; i < 2; ++i) {
            for (int j = 0; j < n; ++j) {
                cin >> grid[i][j];
            }
        }
        vector<pair<LL, LL>> blocks(n);
        for (int i = 0; i < n; ++i) {
            blocks[i] = {grid[0][i], grid[1][i]};
        }
        sort(blocks.begin(), blocks.end(), greater<pair<int, int>>());
        vector<vector<vector<LL>>> dp(n + 1, vector<vector<LL>>(n + 1, vector<LL>(2, -INF)));
        dp[0][0][0] = 0;
        for (int i = 1; i <= n; ++i) {
            for (int j = 0; j <= n; ++j) {
                for (int flag = 0; flag < 2; ++flag) {
                    if (j > 0) {
                        dp[i][j][flag] = max(dp[i][j][flag], dp[i - 1][j - 1][flag] + blocks[i - 1].first);
                    }
                    dp[i][j][flag] = max(dp[i][j][flag], dp[i - 1][j][flag] + blocks[i - 1].second);
                    if (j > 0 && flag == 0) {
                        dp[i][j][1] = max(dp[i][j][1], dp[i - 1][j - 1][0] + blocks[i - 1].first + blocks[i - 1].second);
                    }
                }
            }
        }
        LL ans = -INF;
        for (int j = 0; j <= n; ++j) {
            ans = max(ans, dp[n][j][1]);
        }
        cout << ans << endl;
    }
    return 0;
}