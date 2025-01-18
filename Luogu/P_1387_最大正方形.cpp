#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<vector<int>> M(n, vector<int>(m));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> M[i][j];
        }
    }
    vector<vector<int>> f(n + 1, vector<int>(m + 1, 0));
    int ans = 0;
    for (int i = n - 1; i >= 0; i--) {
        for (int j = m - 1; j >= 0; j--) {
            if (M[i][j] == 0) continue;
            f[i][j] = min({f[i + 1][j], f[i][j + 1], f[i + 1][j + 1]}) + 1;
            ans = max(ans, f[i][j]);
        }
    }
    cout << ans << endl;
    return 0;
}