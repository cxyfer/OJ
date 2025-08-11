/*
Mo's algorithm (帶修改莫隊)

如果答案為 x，則區間長度需至少為 1 + 2 + 3 + 4 + 5 + ... + (x - 1) = x * (x - 1) / 2，
所以求 mex 的時間複雜度為 O(sqrt(N))，直接暴力求 mex 即可。

需要離散化，否則會 TLE。
*/
#include <bits/stdc++.h>
using namespace std;
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
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int N, M; cin >> N >> M;
    vector<int> A(N);
    for (int i = 0; i < N; i++) cin >> A[i];
    auto B = A;  // 收集所有數字用於離散化

    // 離線處理
    int qid = 0, ts = 0;  // query id, timestamp
    vector<Query> queries;
    vector<Record> records;
    for (int i = 0; i < M; i++) {
        int op; cin >> op;
        if (op == 1) {
            int l, r; cin >> l >> r;
            l--;  // 0-indexed, [l, r]
            r--;
            queries.emplace_back(l, r, ts, qid++);
        } else {
            int pos, val; cin >> pos >> val;
            pos--;  // 0-indexed
            // 注意修改時可能會出現新的數字，需要紀錄後才做離散化
            B.push_back(val);
            records.emplace_back(pos, val);
            ts++;
        }
    }

    // 離散化
    sort(B.begin(), B.end());
    B.erase(unique(B.begin(), B.end()), B.end());
    auto get_val = [&](int x) { return lower_bound(B.begin(), B.end(), x) - B.begin(); };
    for (int i = 0; i < N; i++) A[i] = get_val(A[i]);
    for (auto& r : records) r.val = get_val(r.val);

    // Mo's algorithm
    int BLK_SZ = pow(N, 2.0 / 3.0);
    vector<int> cnt(B.size() + 1), cntcnt(N + 1);
    auto add = [&](int x) {
        cntcnt[cnt[x]]--;
        cnt[x]++;
        cntcnt[cnt[x]]++;
    };
    auto del = [&](int x) {
        cntcnt[cnt[x]]--;
        cnt[x]--;
        cntcnt[cnt[x]]++;
    };

    vector<int> ans(queries.size(), -1);
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
        // 暴力求 mex
        int mex = 1;
        while (cntcnt[mex] > 0) mex++;
        ans[q.qid] = mex;
    }
    for (const auto& x : ans) cout << x << endl;
    return 0;
}