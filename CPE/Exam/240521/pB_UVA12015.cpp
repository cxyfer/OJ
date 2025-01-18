#include <bits/stdc++.h>
using namespace std;
const int N = 10;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, kase=1, v;
    string url;
    cin >> t;
    while (t--) {
        vector<pair<string, int>> sites;
        int mx = 0;
        for (int i = 0; i < N; i++) {
            cin >> url >> v;
            sites.push_back({url, v});
            mx = max(mx, v);
        }
        cout << "Case #" << kase++ << ":" << endl;
        for (auto site : sites) {
            if (site.second == mx) {
                cout << site.first << endl;
            }
        }
    }
    return 0;
}