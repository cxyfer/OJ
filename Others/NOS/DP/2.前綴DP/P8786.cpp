/*
P8786 [蓝桥杯 2022 省 B] 李白打酒加强版
https://www.luogu.com.cn/problem/P8786
*/

#include <bits/stdc++.h>
using namespace std;
const int MOD = 1e9 + 7;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int N, M; cin >> N >> M;
    vector<vector<vector<int>>> memo(N + 1, vector<vector<int>>(M + 1, vector<int>(M + 1, -1)));
    auto dfs = [&](this auto&& dfs, int i, int j, int k) -> int {
        if (i == 0) return j > 0 and j == k;
        if (j == 0 or j < k) return 0;
        int &res = memo[i][j][k];
        if (res != -1) return res;
        res = 0;
        if ((k << 1) <= j) res += dfs(i - 1, j, k << 1);
        if (k > 0) res += dfs(i, j - 1, k - 1);
        return res %= MOD;
    };
    cout << dfs(N, M, 2) << endl;
    return 0;
}