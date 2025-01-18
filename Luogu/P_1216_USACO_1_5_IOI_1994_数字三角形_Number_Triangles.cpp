#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int r; cin >> r;
    vector<vector<int>> rows(r, vector<int>(r));
    for (int i = 0; i < r; i++) {
        for (int j = 0; j <= i; j++) {
            cin >> rows[i][j];
        }
    }

    vector<vector<int>> memo(r, vector<int>(r, -INF));
    auto dfs = [&](auto &&dfs, int i, int j) -> int {
        if (i == r - 1) return rows[i][j];
        if (memo[i][j] != -INF) return memo[i][j];
        return memo[i][j] = rows[i][j] + max(dfs(dfs, i + 1, j), dfs(dfs, i + 1, j + 1));
    };
    cout << dfs(dfs, 0, 0) << endl;
    return 0;
}