#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f;
const int N = 55;
const int MT = 205;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, T, M1, M2, st, kase = 1;
    int dist[N], has_train[MT][N][2], dp[MT][N];
    while (cin >> n && n) {
        cin >> T;
        dist[0] = 0;
        for (int i = 1; i < n; i++) cin >> dist[i];
        memset(has_train, 0, sizeof(has_train));
        cin >> M1;
        for (int i = 0; i < M1; i++){
            cin >> st;
            for (int j = 1; j < n; j++) {
                if (st > T) break;
                has_train[st][j][0] = 1;
                st += dist[j];
            }
        }
        cin >> M2;
        for (int i = 0; i < M2; i++){
            cin >> st;
            for (int j = n; j > 1; j--) {
                if (st > T) break;
                has_train[st][j][1] = 1;
                st += dist[j-1];
            }
        }

        memset(dp, 0, sizeof(dp));
        for (int i = 1; i < n; i++) dp[T][i] = INF;
        dp[T][n] = 0;
        for (int i = T-1; i >= 0; i--) {
            for (int j = 1; j <= n; j++) {
                dp[i][j] = dp[i+1][j] + 1;
                if (j < n && has_train[i][j][0] && i+dist[j] <= T) {
                    dp[i][j] = min(dp[i][j], dp[i+dist[j]][j+1]);
                }
                if (j > 1 && has_train[i][j][1] && i+dist[j-1] <= T) {
                    dp[i][j] = min(dp[i][j], dp[i+dist[j-1]][j-1]);
                }
            }
        }
        cout << "Case Number " << kase++ << ": ";
        if (dp[0][1] >= INF) cout << "impossible" << endl;
        else cout << dp[0][1] << endl;
        
    }
    return 0;
}