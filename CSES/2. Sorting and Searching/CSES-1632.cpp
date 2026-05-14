#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

void solve() {
    int n, k;
    cin >> n >> k;
    vector<pair<int, int>> movies(n);
    for (auto& [s, e] : movies) cin >> s >> e;

    sort(movies.begin(), movies.end(),
         [](auto& a, auto& b) { return a.second < b.second; });

    multiset<int> end_times;
    for (int i = 0; i < k; i++) end_times.insert(0);

    int ans = 0;
    for (auto& [s, e] : movies) {
        auto it = end_times.upper_bound(s);
        if (it == end_times.begin()) continue;
        end_times.erase(--it);
        end_times.insert(e);
        ans++;
    }
    cout << ans << endl;
    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}