#include <bits/stdc++.h>
using namespace std;
const long long INF = LLONG_MAX / 2;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<int> R(n);
    for (int i = 0; i < n; i++) {
        cin >> R[i];
    }
    vector<vector<int>> checkpoints(m + 1);
    int cur = 0;
    for (int r : R) {
        if (r == 0) {
            cur++;
        } else {
            checkpoints[cur].push_back(r);
        }
    }
    vector<vector<int>> list_S(m + 1), list_I(m + 1);
    for (int i = 0; i <= m; i++) {
        for (int q : checkpoints[i]) {
            if (q > 0) {
                list_S[i].push_back(q);
            } else {
                list_I[i].push_back(-q);
            }
        }
        sort(list_S[i].begin(), list_S[i].end());
        sort(list_I[i].begin(), list_I[i].end());
    }
    vector<vector<long long>> dp(m + 2, vector<long long>(m + 1, -INF));
    dp[m + 1] = vector<long long>(m + 1, 0);
    for (int p = m; p >= 0; p--) {
        for (int s = 0; s <= m; s++) {
            int i = p - s;
            if (0 <= i && i <= m) {
                long long c = upper_bound(list_S[p].begin(), list_S[p].end(), s) - list_S[p].begin() + 
                              upper_bound(list_I[p].begin(), list_I[p].end(), i) - list_I[p].begin();
                long long res1 = (s < m) ? dp[p + 1][s + 1] + c : -INF;
                long long res2 = (i < m) ? dp[p + 1][s] + c : -INF;
                dp[p][s] = max(res1, res2);
            }
        }
    }
    cout << dp[0][0] << endl;
    return 0;
}