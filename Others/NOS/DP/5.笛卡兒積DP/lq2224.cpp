/*
 * LQ2224 [2022 国赛] 修路
 * https://www.lanqiao.cn/problems/2224/learning/
 */
#include <bits/stdc++.h>
using namespace std;
const double INF = 1e300;
#define endl '\n'

void solve() {
    int n, m, d;
    cin >> n >> m >> d;
    vector<double> A(n + 2, 0), B(m + 2, 0);
    for (int i = 1; i <= n; i++) cin >> A[i];
    for (int i = 1; i <= m; i++) cin >> B[i];
    A[n + 1] = INF;
    B[m + 1] = INF;
    sort(A.begin(), A.end());
    sort(B.begin(), B.end());
    vector<vector<array<double, 2>>> f(n + 2, vector<array<double, 2>>(m + 2, {INF, INF}));
    f[0][0][0] = 0;
    for (int i = 1; i <= n; i++) f[i][0][0] = A[i];
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            f[i][j][0] = min(f[i - 1][j][0] + A[i] - A[i - 1],
                             f[i - 1][j][1] + hypot(A[i] - B[j], d));
            f[i][j][1] = min(f[i][j - 1][1] + B[j] - B[j - 1],
                             f[i][j - 1][0] + hypot(A[i] - B[j], d));
        }
    }
    cout << fixed << setprecision(2) << min(f[n][m][0], f[n][m][1]) << endl;
    return;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    solve();
    return 0;
}