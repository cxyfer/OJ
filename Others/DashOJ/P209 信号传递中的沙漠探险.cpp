#include <bits/stdc++.h>
using namespace std;
const int tgt = 5;
const double INF = 1e18;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n; cin >> n;
    vector<double> x(n), a(n);
    for (int i = 0; i < n; i++) cin >> x[i];
    for (int i = 0; i < n; i++) cin >> a[i];

    vector<vector<double>> memo(n, vector<double>(tgt + 1, -INF));
    auto dfs = [&](auto &&dfs, int i, int j) -> double {
        if (i == n - 1) return j == tgt ? 1.0 : -INF;
        if (j == tgt) return -INF;
        double &res = memo[i][j];
        if (res != -INF) return res;
        for (int k = i + 1; k < n; k++) {
            double den = x[k] - x[i];
            if (den == 0) continue;
            res = max(res, (a[i] + a[k]) / den * dfs(dfs, k, j + 1));
        }
        return res;
    };

    double ans = dfs(dfs, 0, 1);
    if (ans == -INF) cout << "0.0000000000" << endl;
    else cout << fixed << setprecision(10) << ans << endl;
    return 0;
}