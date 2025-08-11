#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f;
#define endl '\n'

struct Query {
    int bid, l, r, qid;
    Query(int bid, int l, int r, int qid) : bid(bid), l(l), r(r), qid(qid) {}
};

struct Backup {
    int x, idx1, idx2;
    Backup(int x, int idx1, int idx2) : x(x), idx1(idx1), idx2(idx2) {}
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int N; cin >> N;
    vector<int> A(N);
    for (int i = 0; i < N; i++) cin >> A[i];

    // 離散化
    auto B = A;
    sort(B.begin(), B.end());
    B.erase(unique(B.begin(), B.end()), B.end());
    auto get_val = [&](int x) { return lower_bound(B.begin(), B.end(), x) - B.begin(); };
    for (int i = 0; i < N; i++) A[i] = get_val(A[i]);

    // Mo's algorithm (只加不刪)
    int max_d = INT_MIN;
    vector<pair<int, int>> mp(B.size() + 1, {INF, -INF});
    auto add = [&](int x, int idx) {
        mp[x].first = min(mp[x].first, idx);
        mp[x].second = max(mp[x].second, idx);
        max_d = max(max_d, mp[x].second - mp[x].first);
    };

    int M; cin >> M;
    vector<int> ans(M, -1);
    vector<Query> queries;
    int BLK_SZ = ceil(N / sqrt(M * 2));
    for (int qid = 0; qid < M; qid++) {
        int l, r; cin >> l >> r;
        l--;  // 0-indexed, [l, r]
        r--;
        if (r - l + 1 > BLK_SZ) {
            queries.emplace_back(l / BLK_SZ, l, r, qid);
        }
        else {
            max_d = INT_MIN;
            fill(mp.begin(), mp.end(), make_pair(INF, -INF));
            for (int i = l; i <= r; i++) add(A[i], i);
            ans[qid] = max_d;
        }
    }

    // 離線排序
    sort(queries.begin(), queries.end(), [](const Query& a, const Query& b) {
        if (a.bid != b.bid) return a.bid < b.bid;
        return a.r < b.r;  // 右端點從小到大
    });

    int r = 0;
    for (int i = 0; i < queries.size(); i++) {
        const auto& q = queries[i];
        int l0 = (q.bid + 1) * BLK_SZ;
        // 遍歷到一個新的 block
        if (i == 0 || q.bid > queries[i - 1].bid) {
            r = l0;  // 右端點移動的起點
            fill(mp.begin(), mp.end(), make_pair(INF, -INF));
            max_d = INT_MIN;
        }
        // 右端點從 r 往右移動到 q.r (包含 q.r)
        while (r <= q.r) {
            add(A[r], r);
            r++;
        }
        // 移動左端點前先備份 max_d
        int tmp_max_d = max_d;
        // 左端點從 l0 向左移動到 q.l (不包含 l0)
        vector<Backup> backups;
        // for (int i = q.l; i < l0; i++) {
        for (int i = l0 - 1; i >= q.l; i--) {
            backups.emplace_back(A[i], mp[A[i]].first, mp[A[i]].second);
            add(A[i], i);
        }
        ans[q.qid] = max_d;
        // 回滾
        max_d = tmp_max_d;
        reverse(backups.begin(), backups.end());
        for (auto& [x, idx1, idx2] : backups) mp[x] = {idx1, idx2};
    }
    for (const auto& x : ans) cout << x << endl;
    return 0;
}