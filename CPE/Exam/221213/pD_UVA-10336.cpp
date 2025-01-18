#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};

void dfs(int x, int y, char ch, vector<string> &mp, vector<vector<bool>> &visited) {
    if (x < 0 || x >= mp.size() || y < 0 || y >= mp[0].size() || visited[x][y] || mp[x][y] != ch) return;
    visited[x][y] = true;
    for (int k = 0; k < 4; k++) {
        dfs(x+dx[k], y+dy[k], ch, mp, visited);
    }
}

bool cmp(pair<char, int> &a, pair<char, int> &b) {
    if (a.second == b.second) return a.first < b.first;
    return a.second > b.second;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, kase=1, n, m;
    cin >> t;
    while (t--) {
        cin >> n >> m;
        vector<string> mp(n);
        for (int i = 0; i < n; i++) cin >> mp[i];
        vector<vector<bool>> visited(n, vector<bool>(m, false));
        map<char, int> cnt0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (!visited[i][j]) {
                    dfs(i, j, mp[i][j], mp, visited);
                    cnt0[mp[i][j]]++;
                }
            }
        }
        vector<pair<char, int>> cnt(cnt0.begin(), cnt0.end()); // convert map to vector for sorting
        sort(cnt.begin(), cnt.end(), cmp);
        cout << "World #" << kase++ << endl;
        for (auto &it: cnt) {
            cout << it.first << ": " << it.second << endl;
        }
    }
    return 0;
}