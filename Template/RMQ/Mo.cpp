/*
Mo's algorithm template
https://www.luogu.com.cn/problem/P2709
*/

#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

struct Query {
    int bid, l, r, qid;
    Query(int bid, int l, int r, int qid) : bid(bid), l(l), r(r), qid(qid) {}
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int N, M, K;
    cin >> N >> M >> K;
    vector<int> A(N);
    for (int i = 0; i < N; i++)
        cin >> A[i];

    // Mo's algorithm
    LL cur = 0;
    unordered_map<int, LL> cnt;
    auto add = [&](int x) {
        cur -= cnt[x] * cnt[x];
        cnt[x]++;
        cur += cnt[x] * cnt[x];
    };
    auto del = [&](int x) {
        cur -= cnt[x] * cnt[x];
        cnt[x]--;
        cur += cnt[x] * cnt[x];
    };
    int BLK_SZ = sqrt(N);
    vector<LL> ans(M);
    vector<Query> queries;
    for (int qid = 0; qid < M; qid++) {
        int l, r;
        cin >> l >> r;
        l--; r--;
        if (r - l > BLK_SZ)
            queries.emplace_back(l / BLK_SZ, l, r, qid);
        else {
            for (int i = l; i <= r; i++)
                add(A[i]);
            ans[qid] = cur;
            cnt.clear();
            cur = 0;
        }
    }
    sort(queries.begin(), queries.end(), [](const Query &a, const Query &b) {
        if (a.bid != b.bid)
            return a.bid < b.bid;
        return a.r < b.r;
    });
    int l = 0, r = -1;
    for (const auto &q : queries) {
        while (l > q.l) add(A[--l]);
        while (r < q.r) add(A[++r]);
        while (l < q.l) del(A[l++]);
        while (r > q.r) del(A[r--]);
        ans[q.qid] = cur;
    }
    for (const auto &x : ans)
        cout << x << endl;
    return 0;
}