#include <bits/stdc++.h>
#include <ranges>
using namespace std;
#define endl '\n'

void solve() {
    int n, k;
    cin >> n >> k;
    vector<pair<int, int>> movies(n);
    for (auto& [s, e] : movies) cin >> s >> e;

    ranges::sort(movies, [](auto& a, auto& b) { return a.second < b.second; });

    multiset<int> ends;
    for (int i = 0; i < k; i++) ends.insert(0);

    int ans = 0;
    for (auto& [s, e] : movies) {
        auto it = ends.upper_bound(s);
        if (it == ends.begin()) continue;
        ends.erase(--it);
        ends.insert(e);
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