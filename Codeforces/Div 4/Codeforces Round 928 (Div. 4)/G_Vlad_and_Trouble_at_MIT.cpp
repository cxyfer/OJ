#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int INF = 0x3f3f3f3f;
const int MOD = 1e9 + 7;
const int N = 100005;

vector<int> g[N];
vector<int> dp1(N), dp2(N);
string S;

void dfs(int u) {
    dp1[u] = 0;
    dp2[u] = 0;
    for (auto v : g[u]) {
        dfs(v);
        dp1[u] += min(dp1[v], dp2[v] + 1);
        dp2[u] += min(dp1[v] + 1, dp2[v]);
    }
    if (S[u] == 'S') dp1[u] = INF;
    else if (S[u] == 'P') dp2[u] = INF;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t;
    cin >> t;
    while (t--) {
        int n; cin >> n;
        for (int i = 0; i < n; ++i) g[i].clear();
        int fa;
        for (int i = 1; i < n; ++i) {
            cin >> fa;
            g[fa - 1].push_back(i);
        }
        cin >> S;
        dfs(0);
        cout << min(dp1[0], dp2[0]) << '\n';
    }
    return 0;
}