/*
由於連接兩個單字的條件是 前一個單字的尾字母 與 後一個單字的頭字母 相同，
因此可以將這個相同的字母視為頂點，將連接兩個單字轉換為連接同一個單字頭尾字母的邊，
即將 a...b -> b...c，轉換為 a -> b -> c，這樣就轉換為 歐拉路徑 問題。
*/

#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, st, ed;
    cin >> n;
    vector<string> words(n);
    for (auto &word : words) cin >> word;
    sort(words.begin(), words.end());

    vector<queue<int>> g(26);
    vector<int> deg(26);
    for (int i = 0; i < n; ++i) {
        st = words[i].front() - 'a';
        ed = words[i].back() - 'a';
        g[st].push(i); // 保存單字(邊)的索引
        deg[st]++;
        deg[ed]--;
    }
    st = -1;
    for (int i = 0; i < 26; ++i) {
        if (deg[i] == 1) {
            st = i;
            break;
        }
    }
    if (st == -1) st = words[0].front() - 'a';

    // Hierholzer's algorithm
    vector<bool> used(n);
    vector<int> path;
    auto dfs = [&](auto &&dfs, int u) -> void {
        while (!g[u].empty()) {
            int idx = g[u].front();
            g[u].pop();
            int v = words[idx].back() - 'a';
            if (used[idx]) continue;
            used[idx] = true;
            dfs(dfs, v);
            path.push_back(idx);
        }
    };
    dfs(dfs, st);

    // 檢查是否形成詞鏈
    if (path.size() != n) {
        cout << "***" << endl;
    }
    else {
        reverse(path.begin(), path.end());
        for (int i = 0; i < n; ++i) {
            cout << words[path[i]] << (i == n - 1 ? '\n' : '.');
        }
    }
    return 0;
}