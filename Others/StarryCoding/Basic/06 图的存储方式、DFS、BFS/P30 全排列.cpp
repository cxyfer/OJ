#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n; cin >> n;

    // vector<int> A(n);
    // for (int i = 0; i < n; i++) A[i] = i + 1;
    // do {
    //     for (int i = 0; i < n; i++) cout << A[i] << ' ';
    //     cout << endl;
    // } while (next_permutation(A.begin(), A.end()));

    vector<int> path;
    vector<bool> vis(n + 1);
    auto dfs = [&](auto &&dfs, int i) -> void {
        if (i == n) {
            for (int i = 0; i < n; i++) cout << path[i] << ' ';
            cout << endl;
            return;
        }
        for (int j = 1; j <= n; j++) {
            if (vis[j]) continue;
            vis[j] = true;
            path.push_back(j);
            dfs(dfs, i + 1);
            path.pop_back();
            vis[j] = false;
        }
    };
    dfs(dfs, 0);

    return 0;
}