#include <bits/stdc++.h>
using namespace std;
const int MAX_C = 1e6 + 5;
#define endl '\n'

struct Pyramid {
    int cubes, X;
    char type;
};

vector<Pyramid> pyramids;
vector<vector<int>> f;

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

    // f[i][c] 表示考慮前 i 個金字塔，使用 c 個方塊所需的最少金字塔數
    f.resize(pyramids.size() + 1, vector<int>(MAX_C + 1, INT_MAX));
    f[0][0] = 0;
    for (int i = 1; i <= pyramids.size(); ++i) {
        auto [cubes, X, type] = pyramids[i - 1];
        for (int c = 0; c <= MAX_C; ++c) {
            if (c >= cubes && f[i - 1][c - cubes] != INT_MAX)
                f[i][c] = min(f[i - 1][c], f[i - 1][c - cubes] + 1);
            else
                f[i][c] = f[i - 1][c];
        }
    }
    return 0;
}();

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int C, kase = 0, m = pyramids.size();
    while (cin >> C && C != 0) {
        cout << "Case " << ++kase << ": ";
        if (f[m][C] == INT_MAX) {
            cout << "impossible" << endl;
        }
        else {
            for (int i = m, k = f[m][C]; i > 0; --i) {
                auto [cubes, X, type] = pyramids[i - 1];
                if (C >= cubes && f[i][C] == f[i - 1][C - cubes] + 1) {
                    cout << X << type << " \n"[k == 1];
                    C -= cubes;
                    --k;
                }
            }
        }
    }
    return 0;
}