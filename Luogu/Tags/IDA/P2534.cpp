#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int INF = 0x3f3f3f3f;
const int MOD = 1e9 + 7;
const int N = 100005;
#define endl '\n'

void solve() {
    int n; cin >> n;
    vector<int> A(n);
    for (auto &x : A) cin >> x;

    // 離散化
    auto B = A;
    sort(B.begin(), B.end());
    unordered_map<int, int> mp;
    for (int i = 0; i < n; i++) mp[B[i]] = i + 1;
    for (auto &x : A) x = mp[x];

    auto heuristic = [&](vector<int> &state) -> int {
        int cnt = 0;
        for (int i = 0; i < n - 1; i++)
            if (abs(state[i] - state[i + 1]) != 1) cnt++;
        if (state[n - 1] != n) cnt++;
        return cnt;
    };

    auto dfs = [&](auto &&dfs, int d, int max_d) -> bool {
        int h = heuristic(A);
        if (d + h > max_d) return false;
        if (h == 0) return true;
        for (int i = 1; i <= n; i++) {
            reverse(A.begin(), A.begin() + i);
            if (dfs(dfs, d + 1, max_d)) return true;
            reverse(A.begin(), A.begin() + i);
        }
        return false;
    };

    for (int max_d = heuristic(A); max_d <= (n - 1) * 2; max_d++) {
        if (dfs(dfs, 0, max_d)) {
            cout << max_d << endl;
            return;
        }
    }
    cout << -1 << endl;
    return;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    solve();
    return 0;
}