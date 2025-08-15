/*
 * P2486 [SDOI2011] 染色
 * https://www.luogu.com.cn/problem/P2486
 * 本題在合併時要考慮左右端點的顏色，具有方向性，因此查詢時要維護兩個方向的資訊
 */
#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

// Heavy Light Decomposition Node
struct HLDNode {
    int val, fa, dep, sz, son, top, dfn;
    HLDNode() : val(0), fa(0), dep(0), sz(0), son(0), top(0), dfn(0) {}
};

struct SegInfo {
    int cnt, lcol, rcol;
    SegInfo() : cnt(0), lcol(0), rcol(0) {}
    SegInfo(int cnt, int lcol, int rcol) : cnt(cnt), lcol(lcol), rcol(rcol) {}

    SegInfo operator+(SegInfo const& other) const {
        if (cnt == 0) return other;
        if (other.cnt == 0) return *this;
        return SegInfo(cnt + other.cnt - (rcol == other.lcol), lcol, other.rcol);
    }

    SegInfo reverse() const { // 反轉方向，用於合併時考慮左右端點的顏色，具有方向性
        return SegInfo(cnt, rcol, lcol);
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
            node->val = SegInfo(1, nums[left], nums[left]);
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
        node->val.cnt = 1;
        node->val.lcol = v;
        node->val.rcol = v;
        node->lazy = v;
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
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int N, M, R = 1;
    cin >> N >> M;

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

    char op;
    int a, b, c;
    while (M--) {
        cin >> op;
        if (op == 'C') {
            cin >> a >> b >> c;
            update(a, b, c);
        } else {
            cin >> a >> b;
            cout << query(a, b).cnt << endl;
        }
    }
    return 0;
}