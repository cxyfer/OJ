#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, n;
    cin >> t;
    while (t--) {
        cin >> n;
        vector<vector<int>> g(n);
        for (int i = 0; i < n - 1; ++i) {
            int u, v;
            cin >> u >> v;
            u--; v--;
            g[u].push_back(v);
            g[v].push_back(u);
        }

        // 相同奇偶性的數，相差是 2 的倍數，故除了相鄰兩數差 2 是質數以外，差值都不是質數
        set<int> evens, odds;
        for (int i = 2; i <= 2 * n; i += 2) evens.insert(i);
        for (int i = 3; i <= 2 * n; i += 2) odds.insert(i);

        vector<int> ans(n);
        ans[0] = 1;
        queue<int> q;
        q.push(0);
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (int v : g[u]) {
                if (ans[v]) continue; // 跳過已經賦值的節點
                if (ans[u] & 1) { // 奇數父節點
                    if (evens.count(ans[u] + 1)) { // 第 1 個 v 可以嘗試選 ans[u] + 1 來轉換奇偶性
                        ans[v] = ans[u] + 1;
                        evens.erase(ans[v]);
                    }
                    else { // 第 2 個以後的 v 選相同奇偶性的數，相差是 2 的倍數，除了 2 以外都不是質數
                        ans[v] = (abs(*odds.begin() - ans[u]) != 2)? *odds.begin() : *odds.rbegin();
                        odds.erase(ans[v]);
                    }
                }
                else { // 偶數父節點
                    if (evens.count(ans[u] + 1)) {
                        ans[v] = ans[u] + 1;
                        evens.erase(ans[v]);
                    }
                    else {
                        ans[v] = (abs(*evens.begin() - ans[u]) != 2)? *evens.begin() : *evens.rbegin();
                        evens.erase(ans[v]);
                    }
                }
                q.push(v);
            }
        }

        for (int x : ans) cout << x << ' ';
        cout << endl;
    }
    return 0;
}