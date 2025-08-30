/*
Mo's algorithm (帶修改莫隊)
除了下標外，其他都和 Luogu P1903 相同
*/
#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int MX_V = 1e6 + 5;
#define endl '\n'

struct Query {
    int l, r, ts, qid;
    Query(int l, int r, int ts, int qid) : l(l), r(r), ts(ts), qid(qid) {}
};

struct Record {
    int pos, val;
    Record(int pos, int val) : pos(pos), val(val) {}
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    int N, M;
    cin >> N >> M;
    vector<int> A(N);
    for (int i = 0; i < N; i++) cin >> A[i];

    // Mo's algorithm
    LL cur = 0;
    // unordered_map<int, int> cnt;  // TLE
    vector<int> cnt(MX_V);
    auto add = [&](int x) {
        cnt[x]++;
        if (cnt[x] == 1) cur++;
    };
    auto del = [&](int x) {
        cnt[x]--;
        if (cnt[x] == 0) cur--;
    };

    // int BLK_SZ = sqrt(N);
    int BLK_SZ = pow(N, 2.0 / 3.0);
    int qid = 0, ts = 0;  // timestamp
    vector<Query> queries;
    vector<Record> records;
    for (int i = 0; i < M; i++) {
        char op;
        cin >> op;
        if (op == 'Q') {
            int l, r;
            cin >> l >> r;
            r--;
            queries.emplace_back(l, r, ts, qid++);
        } else {
            int pos, val;
            cin >> pos >> val;
            records.emplace_back(pos, val);
            ts++;
        }
    }
    vector<LL> ans(qid, -1);
    sort(queries.begin(), queries.end(), [BLK_SZ](const Query& a, const Query& b) {
        if (a.l / BLK_SZ != b.l / BLK_SZ) return a.l / BLK_SZ < b.l / BLK_SZ;
        if (a.r / BLK_SZ != b.r / BLK_SZ) return a.r / BLK_SZ < b.r / BLK_SZ;
        return a.ts < b.ts;
    });

    int l = 0, r = -1, t = 0;
    for (const auto& q : queries) {
        while (l > q.l) add(A[--l]);
        while (r < q.r) add(A[++r]);
        while (l < q.l) del(A[l++]);
        while (r > q.r) del(A[r--]);
        // 時間戳變大，替換
        while (t < q.ts) {
            auto& [pos, val] = records[t];
            if (l <= pos && pos <= r) {
                del(A[pos]);
                add(val);
            }
            swap(A[pos], val);
            t++;
        }
        // 時間戳變小，還原
        while (t > q.ts) {
            t--;
            auto& [pos, val] = records[t];
            if (l <= pos && pos <= r) {
                del(A[pos]);
                add(val);
            }
            swap(A[pos], val);
        }
        ans[q.qid] = cur;
    }
    for (const auto& x : ans) cout << x << endl;
    return 0;
}