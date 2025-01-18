#include <bits/stdc++.h>
using namespace std;
const int N = 505;
#define endl '\n'

int A[N][N], B[N][N], sumA[N][N], sumB[N][N], dp[N][N];

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, m, res1, res2;
    
    while (cin >> n >> m && (n || m)) {
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                cin >> A[i][j];
                sumA[i][j] = sumA[i][j - 1] + A[i][j];
            }
        }
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                cin >> B[i][j];
                sumB[i][j] = sumB[i - 1][j] + B[i][j];
            }
        }
        memset(dp, 0, sizeof(dp));
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                res1 = dp[i - 1][j] + sumA[i][j];
                res2 = dp[i][j - 1] + sumB[i][j];
                dp[i][j] = max(res1, res2);
            }
        }
        cout << dp[n][m] << endl;
    }
    return 0;
}