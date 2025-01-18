#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int N, M;
    while (cin >> N >> M) {
        vector<pair<int, int>> pairs;
        for (int i = 1; i <= N; ++i) {
            for (int j = i + 1; j <= N; ++j) {
                pairs.emplace_back(i, j);
            }
        }

        unordered_map<int, int> cnt_s, cnt_p;
        for (auto [x, y] : pairs) {
            int sum_ = x + y;
            int prod = x * y;
            cnt_s[sum_]++;
            cnt_p[prod]++;
        }

        int m = pairs.size();
        vector<bool> vis(m, false);
        for (int i = 1; i <= M; ++i) {
            for (int j = 0; j < m; ++j) {
                if (vis[j]) continue;
                int prod = pairs[j].first * pairs[j].second;
                int sum_ = pairs[j].first + pairs[j].second;
                if (i & 1) {
                    if (cnt_s[sum_] == 1) {
                        vis[j] = true;
                        cnt_s[sum_]--;
                        cnt_p[prod]--;
                    }
                } else {
                    if (cnt_p[prod] == 1) {
                        vis[j] = true;
                        cnt_p[prod]--;
                        cnt_s[sum_]--;
                    }
                }
            }
        }

        vector<pair<int, int>> ans;
        for (int i = 0; i < m; i++) {
            if (vis[i]) continue;
            if (M & 1) {
                int prod = pairs[i].first * pairs[i].second;
                if (cnt_p[prod] == 1) ans.push_back(pairs[i]);
            } else {
                int sum_ = pairs[i].first + pairs[i].second;
                if (cnt_s[sum_] == 1) ans.push_back(pairs[i]);
            }
        }

        // sort(ans.begin(), ans.end());
        cout << ans.size() << endl;
        for (auto [x, y] : ans) {
            cout << x << " " << y << endl;
        }
    }
    return 0;
}