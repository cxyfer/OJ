/*
 * P2758 编辑距离
 * https://www.luogu.com.cn/problem/P2758
 */
#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

void solve1() {  // Memoization (AC)
    string s, t;
    cin >> s >> t;
    int n = s.size(), m = t.size();
    vector<vector<int>> memo(n, vector<int>(m, -1));
    auto dfs = [&](this auto&& dfs, int i, int j) -> int {
        if (i < 0) return j + 1;
        if (j < 0) return i + 1;
        int& res = memo[i][j];
        if (res != -1) return res;
        return res = min({dfs(i - 1, j) + 1, dfs(i, j - 1) + 1, dfs(i - 1, j - 1) + (s[i] != t[j])});
    };
    cout << dfs(n - 1, m - 1) << endl;
    return;
}

void solve2() {  // 查表法
    string s, t;
    cin >> s >> t;
    int n = s.size(), m = t.size();
    vector<vector<int>> f(n + 1, vector<int>(m + 1));
    for (int i = 0; i <= n; ++i) f[i][0] = i;
    for (int j = 0; j <= m; ++j) f[0][j] = j;
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= m; ++j)
            f[i][j] = min({f[i - 1][j] + 1, f[i][j - 1] + 1, f[i - 1][j - 1] + (s[i - 1] != t[j - 1])});
    cout << f[n][m] << endl;
    return;
}

void solve3() {  // 刷表法
    string s, t;
    cin >> s >> t;
    int n = s.size(), m = t.size();
    s = " " + s + " ";
    t = " " + t + " ";
    auto checkmin = [&](int& a, int b) {
        if (b < a) a = b;
    };
    vector<vector<int>> f(n + 2, vector<int>(m + 2, INT_MAX));
    f[0][0] = 0;
    for (int i = 0; i <= n; ++i)
        for (int j = 0; j <= m; ++j) {
            checkmin(f[i + 1][j], f[i][j] + 1);
            checkmin(f[i][j + 1], f[i][j] + 1);
            checkmin(f[i + 1][j + 1], f[i][j] + (s[i + 1] != t[j + 1]));
        }
    cout << f[n][m] << endl;
    return;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    // solve1();
    // solve2();
    solve3();
    return 0;
}