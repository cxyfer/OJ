#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    string line, su, sv;
    vector<string> words;
    while (getline(cin, line) && !line.empty()) {
        words.push_back(line);
    }
    unordered_map<string, int> node2idx;
    for (int i = 0; i < words.size(); i++) node2idx[words[i]] = i;
    
    vector<pair<int, int>> queries;
    while (cin >> su >> sv) {
        queries.emplace_back(node2idx[su], node2idx[sv]);
    }

    int n = words.size();
    for (int i = 0; i < queries.size(); i++) {
        auto [s, t] = queries[i];

        bool flag = false;
        vector<bool> vis(n);
        vector<int> pre(n, -1);
        queue<int> q;
        q.push(s);
        vis[s] = true;
        while (!q.empty()) {
            int u = q.front(); q.pop();
            if (u == t) {
                flag = true;
                break;
            }
            for (int i = 0; i < words[u].size(); i++) {
                for (char c = 'a'; c <= 'z'; c++) {
                    string v = words[u];
                    if (v[i] == c) continue;
                    v[i] = c;
                    if (node2idx.count(v) && !vis[node2idx[v]]) {
                        vis[node2idx[v]] = true;
                        pre[node2idx[v]] = u;
                        q.push(node2idx[v]);
                    }
                }
            }
        }
        if (flag) {
            vector<int> path;
            for (int v = t; v != -1; v = pre[v]) path.push_back(v);
            reverse(path.begin(), path.end());
            for (int node : path) cout << words[node] << endl;
        } else {
            cout << "No solution." << endl;
        }
        if (i < queries.size() - 1) cout << endl;
    }
    return 0;
}