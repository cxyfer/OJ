#include <bits/stdc++.h>
using namespace std;
const int MAX_K = 6;
const int MAX_C = 1e6;
#define endl '\n'

struct Pyramid {
    int cubes, X;
    char type;
};

vector<Pyramid> pyramids;
vector<vector<vector<int>>> f(MAX_K + 1, vector<vector<int>>(MAX_C + 1));
vector<vector<bool>> g(MAX_K + 1, vector<bool>(MAX_C + 1, false));

auto init = []() {
    // 生成所有可能的金字塔
    for (int s = 0, X = 1; ; ++X) {
        s += X * X;
        if (s > MAX_C) break;
        if (X >= 2) pyramids.push_back({s, X, 'H'});
    }
    for (int s = 0, X = 1; ; X += 2) {
        s += X * X;
        if (s > MAX_C) break;
        int H = (X + 1) / 2;
        if (H >= 2) pyramids.push_back({s, X, 'L'});
    }
    for (int s = 0, X = 2; ; X += 2) {
        s += X * X;
        if (s > MAX_C) break;
        int H = (X + 1) / 2;
        if (H >= 2) pyramids.push_back({s, X, 'L'});
    }
    // 排序，把更優的放在後面
    sort(pyramids.begin(), pyramids.end(), [](const Pyramid& a, const Pyramid& b) {
        if (a.cubes != b.cubes) {
            return a.cubes < b.cubes;
        }
        return a.type > b.type;
    });

    // f[i][k][c] 表示考慮前 i 個金字塔，選了 k 個金字塔，使用 c 個方塊的最佳方案
    // g[i][k][c] 表示是否存在方案
    g[0][0] = true;
    for (int i = 0; i < pyramids.size(); ++i) {
        auto [cubes, X, type] = pyramids[i];
        for (int k = MAX_K; k > 0; --k) {
            for (int c = 0; c <= MAX_C; ++c) {
                if (c + cubes > MAX_C) break;
                if (!g[k - 1][c]) continue;
                // 由於更優的方案在後面，所以直接覆蓋即可
                f[k][c + cubes] = f[k - 1][c];
                f[k][c + cubes].push_back(i);
                g[k][c + cubes] = true;
            }
        }
    }
    return 0;
}();

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int C, kase = 0;
    while (cin >> C && C != 0) {
        cout << "Case " << ++kase << ": ";
        bool ok = false;
        for (int k = 1; k <= MAX_K; ++k) {
            if (!g[k][C]) continue;
            ok = true;
            for (int i = k - 1; i >= 0; --i)
                cout << pyramids[f[k][C][i]].X << pyramids[f[k][C][i]].type << " \n"[i == 0];
            break;
        }
        if (!ok) cout << "impossible" << endl;
    }
    return 0;
}