#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

/*
    根據題意，第 i 個盒子的鑰匙在第 x 個盒子裡，因此可以從 x 向 i 連邊，表示打開 x 就能打開 i。
    由於每個點的入度皆為 1，因此最後會形成一個外向基環樹森林。
    在每個基環樹上的環上選擇一個點打破，便能打開該棵基環樹上的所有盒子。

    因此，我們只需要知道基環樹的數量即可，即連通分量的數量。
*/

class UnionFind {
public:
    int cnt;
    vector<int> fa, sz;
    UnionFind(int n) : fa(n), sz(n), cnt(n) {
        iota(fa.begin(), fa.end(), 0);
        fill(sz.begin(), sz.end(), 1);
    }

    int find(int x) {
        return fa[x] == x ? x : fa[x] = find(fa[x]);
    }

    bool merge(int x, int y) {
        int fx = find(x), fy = find(y);
        if (fx == fy) return false;
        if (sz[fx] < sz[fy]) swap(fx, fy);
        fa[fy] = fx;
        sz[fx] += sz[fy];
        cnt--;
        return true;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, x;
    cin >> n;
    UnionFind uf(n);
    for (int i = 0; i < n; ++i) {
        cin >> x;
        uf.merge(i, x - 1);
    }
    cout << uf.cnt << endl;
    return 0;
}