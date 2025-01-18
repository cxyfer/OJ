#include <bits/stdc++.h>
using namespace std;
const int MOD = 1e6 + 7;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<int> A(n);
    for (int i = 0; i < n; i++) cin >> A[i];

    vector<vector<int>> memo(n, vector<int>(m + 1, -1));
    auto dfs = [&](auto &&dfs, int i, int j) -> int {
        if (i == n) return (j == 0) ? 1 : 0;
        if (j < 0) return 0;
        if (memo[i][j] != -1) return memo[i][j];
        int res = 0;
        for (int k = 0; k <= A[i]; k++) {
            res = (res + dfs(dfs, i + 1, j - k)) % MOD;
        }
        return memo[i][j] = res;
    };
    cout << dfs(dfs, 0, m) << endl;
    return 0;
}