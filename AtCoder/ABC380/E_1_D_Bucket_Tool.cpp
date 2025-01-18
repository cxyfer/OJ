#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

class UnionFind {
public:
    vector<int> pa, sz;
    UnionFind(int n) : pa(n), sz(n, 1) {
        iota(pa.begin(), pa.end(), 0);
    }
    int find(int x) {
        if (pa[x] != x) pa[x] = find(pa[x]);
        return pa[x];
    }
    void merge(int x, int y) {
        int fx = find(x), fy = find(y);
        if (fx == fy) return;
        if (fx > fy) swap(fx, fy); // 按照左端點合併
        pa[fy] = fx;
        sz[fx] += sz[fy];
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, q; cin >> n >> q;
    int op, x, c;
    UnionFind uf(n + 1);
    vector<int> color(n + 1), cnt(n + 1);
    for (int i = 1; i <= n; i++) color[i] = i, cnt[i] = 1;
    while (q--) {
        cin >> op;
        if (op == 1) {
            cin >> x >> c;
            int fx = uf.find(x);
            if (color[fx] == c) continue;
            // 需要修改顏色
            int left = fx - 1, right = fx + uf.sz[fx]; // 左側區間和右側區間
            cnt[color[fx]] -= uf.sz[fx]; // 原本顏色的數量減少這個 component 的大小
            cnt[c] += uf.sz[fx]; // 新顏色的數量增加這個 component 的大小
            color[fx] = c; // 更新這個 component 的顏色
            if (right <= n) { // 檢查是否需要合併右側區間
                int fr = uf.find(right);
                if (color[fr] == c) { // 右側區間的顏色相同
                    uf.merge(fx, fr);
                }
            }
            if (left >= 1) { // 檢查是否需要合併左側區間
                int fl = uf.find(left);
                if (color[fl] == c) { // 左側區間的顏色相同
                    uf.merge(fx, fl);
                }
            }
        } else {
            cin >> c;
            cout << cnt[c] << endl;
        }
    }
    return 0;
}