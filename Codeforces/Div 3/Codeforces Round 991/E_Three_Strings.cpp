/*
    題意為在 a 和 b 中由前往後選擇字元，使得與 c 的差異最小。

    首先考慮由前往後推，定義 dfs(i, j) 為 a 已經選擇 i 個字元，b 已經選擇 j 個字元的最小差異。
    則此時有兩種選擇：
        1. 選 a[i]，得 dfs(i + 1, j) + (a[i] != c[i + j])
        2. 選 b[j]，得 dfs(i, j + 1) + (b[j] != c[i + j])
    兩者取最小值即可。最後取 dfs(0, 0) 做為入口。

    也可以由後往前反推，定義 dfs(i, j) 為 a 還有 i 個字元未選，b 還有 j 個字元未選的最小差異。
*/

#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t;
    string a, b, c;
    cin >> t;
    while (t--) {
        cin >> a >> b >> c;
        int m = a.size(), n = b.size();
        vector<vector<int>> memo(m + 1, vector<int>(n + 1, INF));
        auto dfs = [&](auto &&dfs, int i, int j) -> int {
            if (i == m && j == n) return 0;
            int &res = memo[i][j];
            if (res != INF) return res;
            res = INF;
            if (i < m) res = min(res, dfs(dfs, i + 1, j) + (a[i] != c[i + j])); // 選 a[i]
            if (j < n) res = min(res, dfs(dfs, i, j + 1) + (b[j] != c[i + j])); // 選 b[j]
            return res;
        };
        cout << dfs(dfs, 0, 0) << endl;
    }
    return 0;
}