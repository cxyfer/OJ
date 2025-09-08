/*
P12211 [蓝桥杯 2023 国 Python B] 翻转
https://www.luogu.com.cn/problem/P12211
*/

#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n; cin >> n;
    vector<string> s(n);
    for (int i = 0; i < n; i++) cin >> s[i];

    vector<vector<int>> memo(n, vector<int>(26, -1));
    auto dfs = [&](this auto&& dfs, int i, int c) -> int {
        if (i == n) return 0;
        int& res = memo[i][c];
        if (res != -1) return res;
        int c1 = s[i][0] - 'a', c2 = s[i][1] - 'a';
        res = min(dfs(i + 1, c2) + (i > 0 && c1 == c ? 1 : 2),
                dfs(i + 1, c1) + (i > 0 && c2 == c ? 1 : 2));
        return res;
    };
    cout << dfs(0, 0) << endl;
    return 0;
}