#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n; cin >> n;
    vector<int> A(n), s(n + 1);
    for (int i = 0; i < n; i++) cin >> A[i];
    for (int i = 1; i <= n; i++) s[i] = s[i - 1] + A[i - 1];
    vector<vector<int>> memo(n, vector<int>(n, -1));
    auto dfs = [&](auto &&dfs, int l, int r) -> int {
        if (l == r) return 0;
        if (memo[l][r] != -1) return memo[l][r];
        int res = INT_MAX;
        for (int i = l; i < r; i++) {
            res = min(res, dfs(dfs, l, i) + dfs(dfs, i + 1, r) + s[r + 1] - s[l]);
        }
        return memo[l][r] = res;
    };
    cout << dfs(dfs, 0, n - 1) << endl;
    return 0;
}