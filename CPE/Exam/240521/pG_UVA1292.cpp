/*
    AC: UVA, CPE, ZeroJudge
*/
#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

vector<vector<int>> g;
vector<vector<int>> dp;

void dfs(int u, int fa) {
    dp[u][0] = 0;
    dp[u][1] = 1;
    for (int v : g[u]) {
        if (v == fa) {
            continue;
        }
        dfs(v, u);
        dp[u][0] += dp[v][1];
        dp[u][1] += min(dp[v][0], dp[v][1]);
    }
}

int main() {
    // 混用 cin/cout 和 scanf/printf 就不能取消同步
    // ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, u, d, v;
    while (cin >> n && n) {
        g.clear();
        g.resize(n);
        dp.clear();
        dp.resize(n, vector<int>(2, 0));
        for (int i=0; i<n; i++) {
            scanf("%d:(%d)", &u, &d);
            int v;
            for (int j=0; j<d; j++) {
                cin >> v;
                g[u].push_back(v);
                g[v].push_back(u);
            }
        }
        dfs(0, -1);
        cout << min(dp[0][0], dp[0][1]) << endl;
    }
    return 0;
}