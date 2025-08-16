/*
 * P3976 [TJOI2015] 旅游
 * https://www.luogu.com.cn/problem/P3976
 * 和 P2486 類似，本題在合併時也要考慮方向性
 */
#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f;
#define endl '\n'

// Heavy Light Decomposition Node
struct HLDNode {
    int val, fa, dep, sz, son, top, dfn;
    HLDNode() : val(0), fa(0), dep(0), sz(0), son(0), top(0), dfn(0) {}
};

struct SegInfo {
    int mx, mn, lgain, rgain;
    SegInfo() : mx(-INF), mn(INF), lgain(0), rgain(0) {}
    SegInfo(int mx, int mn, int lgain, int rgain)
        : mx(mx), mn(mn), lgain(lgain), rgain(rgain) {}

    SegInfo operator+(SegInfo const& other) const {
        return SegInfo(max(mx, other.mx), min(mn, other.mn),
                       max({lgain, other.lgain, other.mx - mn}),
                       max({rgain, other.rgain, mx - other.mn}));
    }

    SegInfo reverse() const {  // 反轉方向
        return SegInfo(mx, mn, rgain, lgain);
    }
};

struct SegNode {
    SegNode *ls, *rs;  // left child, right child
    SegInfo val;       // value, lazy tag
    int lazy;          // lazy tag
    SegNode() : ls(nullptr), rs(nullptr), val(SegInfo()), lazy(0) {}
};

class SegmentTree {
public:
    SegmentTree(vector<int>& nums) {
        n = nums.size() - 1;
        root = new SegNode();
        build(root, 1, n, nums);
    }

    void update(int l, int r, int v) {
        _update(root, 1, n, l, r, v);
    }

    SegInfo query(int l, int r) {
        return _query(root, 1, n, l, r);
    }

private:
    int n;
    SegNode* root;
    void build(SegNode* node, int left, int right, vector<int>& nums) {
        if (left == right) {
            node->val = SegInfo(nums[left], nums[left], 0, 0);
            return;
        }
        int mid = left + ((right - left) >> 1);
        node->ls = new SegNode();
        node->rs = new SegNode();
        build(node->ls, left, mid, nums);
        build(node->rs, mid + 1, right, nums);
        pushup(node);  // Push up node value
    }

    // Update the range [l, r] with value v
    void _update(SegNode* node, int left, int right, int l, int r, int v) {
        if (l <= left && right <= r) {
            // Update node value (Customized)
            apply(node, left, right, v);
            return;
        }
        pushdown(node, left, right);
        int mid = left + ((right - left) >> 1);
        if (l <= mid) _update(node->ls, left, mid, l, r, v);
        if (r > mid) _update(node->rs, mid + 1, right, l, r, v);
        pushup(node);  // Push up node value
    }

    // Update node value (Customized)
    void apply(SegNode* node, int left, int right, int v) {
        node->val.mx += v;
        node->val.mn += v;
        node->lazy += v;
    }

    // Query the range [l, r]
    SegInfo _query(SegNode* node, int left, int right, int l, int r) {
        if (l <= left && right <= r) {
            return node->val;
        }
        pushdown(node, left, right);
        int mid = left + ((right - left) >> 1);
        // Calculate answer (Customized)
        SegInfo ans = SegInfo();
        if (l <= mid) ans = ans + _query(node->ls, left, mid, l, r);
        if (r > mid) ans = ans + _query(node->rs, mid + 1, right, l, r);
        return ans;
    }

    // Push down lazy tags
    void pushdown(SegNode* node, int left, int right) {
        if (node->ls == nullptr) node->ls = new SegNode();
        if (node->rs == nullptr) node->rs = new SegNode();
        if (node->lazy != 0) {
            int mid = left + ((right - left) >> 1);
            // Update node value (Customized)
            apply(node->ls, left, mid, node->lazy);
            apply(node->rs, mid + 1, right, node->lazy);
            node->lazy = 0;
        }
    }

    // Push up node value
    void pushup(SegNode* node) {
        // Update method (Customized)
        node->val = node->ls->val + node->rs->val;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    int N, M, R = 1;
    cin >> N;

    vector<HLDNode> A(N + 1);
    for (int i = 1; i <= N; i++) cin >> A[i].val;

    vector<vector<int>> g(N + 1);
    for (int i = 1; i < N; i++) {
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }

    auto dfs1 = [&](this auto&& dfs1, int u, int fa) -> void {
        A[u].fa = fa;
        A[u].dep = A[fa].dep + 1;
        A[u].sz = 1;
        for (int v : g[u]) {
            if (v == fa) continue;
            dfs1(v, u);
            A[u].sz += A[v].sz;
            if (A[u].son == 0 || A[A[u].son].sz < A[v].sz) A[u].son = v;
        }
        return;
    };
    dfs1(R, 0);

    int dfn = 0;
    vector<int> idxs(N + 1);  // dfn -> idx
    auto dfs2 = [&](this auto&& dfs2, int u, int top) -> void {
        if (u == 0) return;
        A[u].top = top;
        A[u].dfn = ++dfn;
        idxs[dfn] = u;
        dfs2(A[u].son, top);  // 先遍歷重鏈
        for (int v : g[u]) {
            if (v == A[u].fa || v == A[u].son) continue;
            dfs2(v, v);
        }
        return;
    };
    dfs2(R, R);

    vector<int> vals(N + 1);
    for (int i = 1; i <= N; i++) vals[A[i].dfn] = A[i].val;
    SegmentTree seg(vals);

    // 更新路徑 (a, b) 的資訊
    auto update = [&](int x, int y, int v) -> void {
        while (A[x].top != A[y].top) {
            if (A[A[x].top].dep >= A[A[y].top].dep) {
                // 重鏈區間：從 top[x] 到 x
                seg.update(A[A[x].top].dfn, A[x].dfn, v);
                // 跳到整條重鏈的上一層
                x = A[A[x].top].fa;
            } else {
                seg.update(A[A[y].top].dfn, A[y].dfn, v);
                y = A[A[y].top].fa;
            }
        }
        int l = min(A[x].dfn, A[y].dfn), r = max(A[x].dfn, A[y].dfn);
        seg.update(l, r, v);
        return;
    };

    auto query = [&](int x, int y) -> SegInfo {
        // 查詢 x -> LCA -> y 的區間資訊
        // 由於合併時要考慮左右端點的顏色，具有方向性，因此要維護兩個方向的資訊
        SegInfo ansL = SegInfo(), ansR = SegInfo();
        while (A[x].top != A[y].top) {
            if (A[A[x].top].dep >= A[A[y].top].dep) {
                // x -> x.top 相比線段樹的合併方向是反向，翻轉後向左合併
                ansL = ansL + seg.query(A[A[x].top].dfn, A[x].dfn).reverse();
                x = A[A[x].top].fa;
            } else {
                // y.top -> y 是正向，直接向右合併
                ansR = seg.query(A[A[y].top].dfn, A[y].dfn) + ansR;
                y = A[A[y].top].fa;
            }
        }
        if (A[x].dfn > A[y].dfn)  // y 在 x 的上方，翻轉後合併
            return ansL + seg.query(A[y].dfn, A[x].dfn).reverse() + ansR;
        else  // x 在 y 的上方，直接合併
            return ansL + seg.query(A[x].dfn, A[y].dfn) + ansR;
    };

    cin >> M;
    int a, b, v;
    while (M--) {
        cin >> a >> b >> v;
        cout << query(a, b).lgain << endl;
        update(a, b, v);
    }
    return 0;
}