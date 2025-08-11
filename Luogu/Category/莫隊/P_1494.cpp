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
    int N, M;
    cin >> N >> M;
    vector<int> A(N);
    for (int i = 0; i < N; i++)
        cin >> A[i];

    // Mo's algorithm
    LL cur = 0;
    // unordered_map<int, LL> cnt;
    vector<LL> cnt(N + 1);
    auto add = [&](int x) {
        // cur -= cnt[x] * (cnt[x] - 1LL) / 2;
        cur += cnt[x];
        cnt[x]++;
        // cur += cnt[x] * (cnt[x] - 1LL) / 2;
    };
    auto del = [&](int x) {
        // cur -= cnt[x] * (cnt[x] - 1LL) / 2;
        cnt[x]--;
        cur -= cnt[x];
        // cur += cnt[x] * (cnt[x] - 1LL) / 2;
    };

    // int BLK_SZ = ceil(1.0 * N / sqrt(M * 2));
    int BLK_SZ = sqrt(N);
    vector<pair<LL, LL>> ans(M);
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
            ans[qid] = {cur, (r - l + 1LL) * (r - l) / 2};
            // cnt.clear();
            fill(cnt.begin(), cnt.end(), 0);
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
        ans[q.qid] = {cur, (r - l + 1LL) * (r - l) / 2};
    }
    for (const auto &[num, den] : ans) {
        if (den == 0) {
            cout << "0/1" << endl;
            continue;
        }
        int g = __gcd(num, den);
        cout << num / g << "/" << den / g << endl;
    }
    return 0;
}