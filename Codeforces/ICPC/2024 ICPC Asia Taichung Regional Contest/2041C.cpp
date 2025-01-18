#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const LL INF = 0x3f3f3f3f3f3f3f3f;
#define endl '\n'

/*
由於要選 n 個數，因此其實每個 x = 0, 1, 2, ..., n - 1 都會選一個
考慮每個 x 平面上選擇哪個數字，維護 y_mask 和 z_mask 兩個狀態表示已經選擇的數
狀態數量為 O(n * 2^n * 2^n) = O(n * 2^2n)
轉移時枚舉 n^2 個數字，因此總時間複雜度為 O(n^3 * 2^2n)
*/

int n;
vector<vector<vector<int>>> cube;
vector<vector<vector<int>>> memo;
int mask;

LL dfs(int i, int y, int z) {
    if (i == n) {
        return 0;
    }
    if (memo[i][y][z] != -1) {
        return memo[i][y][z];
    }
    LL res = INF;
    for (int j = 0; j < n; j++) {
        if (y >> j & 1) continue;
        for (int k = 0; k < n; k++) {
            if (z >> k & 1) continue;
            res = min(res, cube[i][j][k] + dfs(i + 1, y | (1 << j), z | (1 << k)));
        }
    }
    return memo[i][y][z] = res;
}

int main() {
    cin >> n;
    mask = (1 << n) - 1;
    cube.resize(n, vector<vector<int>>(n, vector<int>(n)));
    memo.resize(n, vector<vector<int>>(mask + 1, vector<int>(mask + 1, -1)));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < n; k++) {
                cin >> cube[i][j][k];
            }
        }
    }
    cout << dfs(0, 0, 0) << endl;
    return 0;
}