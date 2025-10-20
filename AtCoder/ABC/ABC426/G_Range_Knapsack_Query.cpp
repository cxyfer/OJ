#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

struct Item {
    int w, v;
    Item() : w(0), v(0) {}
    Item(int w, int v) : w(w), v(v) {}
};

struct Query {
    int qid, l, r, c;
    Query(int qid, int l, int r, int c) : qid(qid), l(l), r(r), c(c) {}
};

void solve() {
    int n, q, l, r, c;
    cin >> n;
    vector<Item> items(n + 1);
    for (int i = 1; i <= n; i++) cin >> items[i].w >> items[i].v;
    cin >> q;
    vector<LL> ans(q, -1);
    vector<Query> queries;
    for (int qid = 0; qid < q; qid++) {
        cin >> l >> r >> c;
        if (l == r) ans[qid] = (items[l].w <= c ? items[l].v : 0);
        else queries.push_back(Query(qid, l, r, c));
    }

    int MAX_C = 0;
    for (auto &query : queries) MAX_C = max(MAX_C, query.c);
    vector<vector<LL>> fl(n + 1, vector<LL>(MAX_C + 1, 0)), fr(n + 1, vector<LL>(MAX_C + 1, 0));
    // Divide and conquer
    auto dfs = [&](auto &&dfs, int left, int right, vector<Query> &queries) -> void {
        if (queries.empty() || left >= right) return;
        int mid = left + ((right - left) >> 1);
        // Divide into three parts: left, across middle, right
        vector<Query> ql, qm, qr;
        for (auto &query : queries) {
            if (query.l <= mid && query.r > mid) qm.push_back(query);
            else if (query.r <= mid) ql.push_back(query);
            else qr.push_back(query);
        }
        dfs(dfs, left, mid, ql);
        dfs(dfs, mid + 1, right, qr);
        if (!qm.empty()) {
            int C = ranges::max(qm | views::transform(&Query::c));
            for (int c = 0; c <= C; c++)
                fl[mid + 1][c] = fr[mid][c] = 0;
            // fl: knapsack on [left, mid] (from right to left)
            for (int i = mid; i >= left; i--) {
                auto [w, v] = items[i];
                for (int c = 0; c <= C; c++) {
                    if (c >= w) fl[i][c] = max(fl[i + 1][c], fl[i + 1][c - w] + v);
                    else fl[i][c] = fl[i + 1][c];
                }
            }
            // fr: knapsack on [mid + 1, right] (from left to right)
            for (int i = mid + 1; i <= right; i++) {
                auto [w, v] = items[i];
                for (int c = 0; c <= C; c++) {
                    if (c >= w) fr[i][c] = max(fr[i - 1][c], fr[i - 1][c - w] + v);
                    else fr[i][c] = fr[i - 1][c];
                }
            }
            // Merge the results of fl and fr for each query
            for (auto &[qid, l, r, c] : qm)
                for (int cc = 0; cc <= c; cc++)
                    ans[qid] = max(ans[qid], fl[l][cc] + fr[r][c - cc]);
        }
        return;
    };
    dfs(dfs, 1, n, queries);
    for (auto &x : ans) cout << x << endl;
    return;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    solve();
    return 0;
}