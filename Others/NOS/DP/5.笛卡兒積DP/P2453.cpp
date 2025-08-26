/*
 * P2453 [SDOI2006] 最短距离
 * https://www.luogu.com.cn/problem/P2453
 * 注意 kill 操作是應用在後綴上，如果用前綴定義狀態的話要另外處理
 */
#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

void solve1() {
    int dlt, rep, cpy, ins, twi;
    string s, t;
    cin >> s >> t >> dlt >> rep >> cpy >> ins >> twi;
    int n = s.size(), m = t.size();
    // dfs(i, j)：將源串的「後綴」 s[i:] 轉換為目標串的「後綴」 t[j:] 所需的最小代價。
    vector<vector<int>> memo(n, vector<int>(m, -1));
    auto dfs = [&](this auto&& dfs, int i, int j) -> int {
        if (i == n && j == m) return 0;
        if (i == n) return (m - j) * ins;
        if (j == m) return (n - i) * dlt - 1;
        int& res = memo[i][j];
        if (res != -1) return res;
        res = min({dfs(i + 1, j) + dlt, dfs(i, j + 1) + ins,
                   dfs(i + 1, j + 1) + rep});
        if (cpy < rep && s[i] == t[j]) res = min(res, dfs(i + 1, j + 1) + cpy);
        if (i < n - 1 && j < m - 1 && s[i] == t[j + 1] && s[i + 1] == t[j])
            res = min(res, dfs(i + 2, j + 2) + twi);
        return res;
    };
    cout << dfs(0, 0) << endl;
    return;
}

void solve2() {
    int dlt, rep, cpy, ins, twi;
    string s, t;
    cin >> s >> t >> dlt >> rep >> cpy >> ins >> twi;
    int n = s.size(), m = t.size();
    // dfs(i, j)：將源串的「前綴」 s[:i+1] 轉換為目標串的「前綴」 t[:j+1] 所需的最小代價。
    vector<vector<int>> memo(n, vector<int>(m, -1));
    auto dfs = [&](this auto&& dfs, int i, int j) -> int {
        if (i < 0 && j < 0) return 0;
        if (i < 0) return (j + 1) * ins;
        if (j < 0) return (i + 1) * dlt;
        int& res = memo[i][j];
        if (res != -1) return res;
        res = min({dfs(i - 1, j) + dlt, dfs(i, j - 1) + ins,
                   dfs(i - 1, j - 1) + rep});
        if (cpy < rep && s[i] == t[j]) res = min(res, dfs(i - 1, j - 1) + cpy);
        if (i > 0 && j > 0 && s[i] == t[j - 1] && s[i - 1] == t[j])
            res = min(res, dfs(i - 2, j - 2) + twi);
        return res;
    };
    int ans = dfs(n - 1, m - 1);
    for (int i = n - 2; i >= 0; --i)
        ans = min(ans, dfs(i, m - 1) + (n - 1 - i) * dlt - 1);
    cout << ans << endl;
    return;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    // solve1();
    solve2();
    return 0;
}