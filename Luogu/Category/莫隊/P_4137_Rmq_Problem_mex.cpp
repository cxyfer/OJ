#include <bits/stdc++.h>
using namespace std;
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
    for (int i = 0; i < N; i++) cin >> A[i];

    // Mo's algorithm (只刪不加)
    // unordered_map<int, int> cnt0, cnt; // TLE
    vector<int> cnt0(N + 1), cnt(N + 1);
    int mex = 0, mex0 = 0;
    // 預處理整個陣列的 mex
    for (auto x : A)
        // 大於 N 的數字不會影響 mex
        if (x <= N) cnt0[x]++;
    while (cnt0[mex0] > 0) mex0++;

    auto del = [&](int x) {
        if (x <= N && --cnt[x] == 0) mex = min(mex, x);
    };

    // int BLK_SZ = sqrt(N);
    int BLK_SZ = ceil(N / sqrt(M * 2));

    vector<int> ans(M);
    vector<Query> queries;
    for (int qid = 0; qid < M; qid++) {
        int l, r;
        cin >> l >> r;
        l--;  // 0-indexed, [l, r]
        r--;
        // 大區間離線，確保 l 和 r 不在同一個 block 中
        if (r - l + 1 > BLK_SZ) queries.emplace_back(l / BLK_SZ, l, r, qid);
        // 小區間暴力
        else {
            fill(cnt.begin(), cnt.end(), 0);
            mex = 0;
            for (int i = l; i <= r; i++)
                if (A[i] <= N) cnt[A[i]]++;
            // mex 最多移動 BLK_SZ 次
            while (cnt[mex] > 0) mex++;
            ans[qid] = mex;
        }
    }

    // 離線排序
    sort(queries.begin(), queries.end(), [](const Query& a, const Query& b) {
        if (a.bid != b.bid) return a.bid < b.bid;
        return a.r > b.r;  // 右端點從大到小
    });

    int l = 0, r = 0;
    for (int i = 0; i < queries.size(); i++) {
        const auto& q = queries[i];
        int l0 = q.bid * BLK_SZ;
        // 遍歷到一個新的 block
        if (i == 0 || q.bid > queries[i - 1].bid) {
            // 左端點刪到 l0，這裡直接對 cnt0 進行操作
            for (; l < l0; l++)
                if (A[l] <= N && --cnt0[A[l]] == 0) mex0 = min(mex0, A[l]);
            // 複製 cnt0 到 cnt
            cnt = cnt0;
            mex = mex0;
            // 設定右端點
            r = N - 1;
        }
        // 右端點從 r 移動到 q.r (不包含 q.r)
        while (q.r < r) del(A[r--]);
        // 移動左端點前先備份 mex
        int tmp_mex = mex;
        // 左端點從 l0 移動到 q.l (不包含 q.l)
        for (int i = l0; i < q.l; i++) del(A[i]);
        ans[q.qid] = mex;

        // 回滾
        mex = tmp_mex;
        for (int i = l0; i < q.l; i++)
            if (A[i] <= N) cnt[A[i]]++;
    }
    for (const auto& x : ans) cout << x << endl;
    return 0;
}