#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

void solve() {
    int n, m;
    cin >> n >> m;
    vector<string> grid(n);
    for (int i = 0; i < n; i++) cin >> grid[i];

    vector<vector<int>> memo(n, vector<int>(m, -1));
    auto dfs = [&](this auto&& dfs, int i, int j) -> int {
        if (i < 0 || i >= n || j < 0 || j >= m) return 0;
        int& res = memo[i][j];
        if (res != -1) return res;
        res = 1;
        if (grid[i][j] == 'U') return res = dfs(i - 1, j);
        else if (grid[i][j] == 'D') return res = dfs(i + 1, j);
        else if (grid[i][j] == 'L') return res = dfs(i, j - 1);
        else if (grid[i][j] == 'R') return res = dfs(i, j + 1);
        else return res = dfs(i - 1, j) || dfs(i + 1, j) || dfs(i, j - 1) || dfs(i, j + 1);
    };
    
    int ans = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            ans += dfs(i, j);
    cout << ans << endl;
    return;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}