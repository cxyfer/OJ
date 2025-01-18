#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, n, s;
    cin >> t;
    while (t--) {
        cin >> n >> s;
        vector<set<int>> g(n + 1);
        vector<int> cnt(n + 1);
        for (int i = 0; i < s; i++) {
            vector<int> arr;
            int x;
            while (cin >> x && x) {
                arr.push_back(x);
            }
            cnt[arr[0]]++;
            for (int i = 1; i < arr.size(); i++) {
                int u = arr[i - 1], v = arr[i];
                g[u].insert(v);
                g[v].insert(u);
                cnt[v]++;
            }
        }
        vector<int> importants;
        for (int i = 1; i <= n; i++) {
            if (cnt[i] > 1) {
                importants.push_back(i);
            }
        }
        int ans = importants[0];
        int mn = INF;
        for (int x : importants) {
            queue<pair<int, int>> q;
            vector<bool> visited(n + 1);
            vector<int> dist(n + 1, INF);
            dist[x] = 0;
            visited[x] = true;
            q.push({x, 0});
            bool all_visited = false;
            while (!q.empty() && !all_visited) {
                // auto [u, d] = q.front();
                pair<int, int> p = q.front(); q.pop();
                int u = p.first, d = p.second;
                for (int v : g[u]) {
                    if (!visited[v]) {
                        visited[v] = true;
                        dist[v] = d + 1;
                        q.push({v, d + 1});
                    }
                }
                all_visited = true;
                for (int y : importants) {
                    if (!visited[y]) {
                        all_visited = false;
                        break;
                    }
                }
            }
            int d_sum = 0;
            for (int y : importants) {
                d_sum += dist[y];
            }
            if (d_sum < mn) {
                mn = d_sum;
                ans = x;
            }
        }
        cout << "Krochanska is in: " << ans << endl;
        
    }
    return 0;
}