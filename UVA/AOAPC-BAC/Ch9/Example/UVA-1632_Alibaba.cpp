/*
    區間DP
    dp[i][j][0/1]: 訪問區間 [i,j] 時所需時間，且最後一次訪問點在 i/j
    tags: DP, 區間DP, 紫書-Ch9, CPE-151006
    reference: https://blog.csdn.net/qq_37656398/article/details/81634469
*/
#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f;
const int N = 1e4 + 5;
#define endl '\n'

int n;
int a[N], b[N];
int dp[N][N][2];

int main() {
    // while (cin >> n) {
    while (scanf("%d", &n) == 1) {
        // for (int i = 0; i < n; i++) cin >> a[i] >> b[i];
        // memset(dp, 0, sizeof(dp));
        for (int i = 0; i < n; i++){
            //  cin >> a[i] >> b[i];
            scanf("%d %d", &a[i], &b[i]);
            // dp[i][i][0] = dp[i][i][1] = 0;
        }
        memset(dp, 0, sizeof(dp));
        for (int i = n-2; i >= 0; i--) {
            for (int j = i+1; j < n; j++) {
                dp[i][j][0] = min(dp[i+1][j][0] + a[i+1] - a[i], dp[i+1][j][1] + a[j] - a[i]);
                if (dp[i][j][0] >= b[i]) dp[i][j][0] = INF;
                dp[i][j][1] = min(dp[i][j-1][0] + a[j] - a[i], dp[i][j-1][1] + a[j] - a[j-1]);
                if (dp[i][j][1] >= b[j]) dp[i][j][1] = INF;
            }
        }
        // int ans = min(dp[0][n-1][0], dp[0][n-1][1]);
        // cout << (ans != INF ? to_string(ans) : "No solution") << endl;
        if (dp[0][n-1][0] == INF && dp[0][n-1][1] == INF) {
            // cout << "No solution" << endl;
            puts("No solution");
        } else {
            // cout << min(dp[0][n-1][0], dp[0][n-1][1]) << endl;
            printf("%d\n", min(dp[0][n-1][0], dp[0][n-1][1]));
        }
    }
    return 0;
}
