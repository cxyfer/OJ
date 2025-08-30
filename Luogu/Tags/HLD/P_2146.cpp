/*
 * P2146 [NOI2015] 软件包管理器
 * https://www.luogu.com.cn/problem/P2146
 * 0-indexed
 */
#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

struct Node {
    int val, fa, dep, sz, son, top, dfn;
    Node() : val(0), fa(-1), dep(0), sz(0), son(-1), top(-1), dfn(0) {}
};

template <typename T>
struct SegNode {
    SegNode *ls, *rs;
    T val;     // 區間內 1 的個數
    int lazy;  // -1: 無標記；0/1: 全區間要賦值為 0 或 1
    SegNode() : ls(nullptr), rs(nullptr), val(0), lazy(-1) {}
};

template <typename T>
class SegmentTree {
public:
    SegmentTree(int n) : n(n) {
        root = new SegNode<T>();
    }

    // 將區間 [l,r] 全部設為 v (0 或 1)
    void update(int l, int r, int v) {
        _update(root, 0, n - 1, l, r, v);
    }

    // 回傳區間 [0,n-1] 中 1 的數量
    int query() {
        return _query(root, 0, n - 1, 0, n - 1);
    }

private:
    int n;
    SegNode<T>* root;

    void _update(SegNode<T>* node, int left, int right, int l, int r, int v) {
        if (l <= left && right <= r) {
            _apply(node, left, right, v);
            return;
        }
        pushdown(node, left, right);
        int mid = left + ((right - left) >> 1);
        if (l <= mid) _update(node->ls, left, mid, l, r, v);
        if (r > mid) _update(node->rs, mid + 1, right, l, r, v);
        pushup(node);
    }

    void _apply(SegNode<T>* node, int left, int right, int v) {
        node->val = v * (right - left + 1);
        node->lazy = v;
    }

    T _query(SegNode<T>* node, int left, int right, int l, int r) {
        if (!node) return 0;
        if (l <= left && right <= r) {
            return node->val;
        }
        pushdown(node, left, right);
        int mid = left + ((right - left) >> 1);
        T ans = 0;
        if (l <= mid) ans += _query(node->ls, left, mid, l, r);
        if (r > mid) ans += _query(node->rs, mid + 1, right, l, r);
        return ans;
    }

    void pushdown(SegNode<T>* node, int left, int right) {
        if (node->ls == nullptr) node->ls = new SegNode<T>();
        if (node->rs == nullptr) node->rs = new SegNode<T>();
        if (node->lazy != -1) {
            int mid = left + ((right - left) >> 1);
            _apply(node->ls, left, mid, node->lazy);
            _apply(node->rs, mid + 1, right, node->lazy);
            node->lazy = -1;  // 清空 lazy
        }
    }

    void pushup(SegNode<T>* node) {
        node->val = 0;
        if (node->ls) node->val += node->ls->val;
        if (node->rs) node->val += node->rs->val;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int N, M;
    cin >> N;

    vector<Node> A(N);
    vector<vector<int>> g(N);
    for (int u, v = 1; v < N; v++) {
        cin >> u;
        g[u].push_back(v);
    }

    auto dfs1 = [&](this auto&& dfs1, int u, int fa) -> void {
        A[u].fa = fa;
        A[u].dep = (fa == -1 ? 0 : A[fa].dep) + 1;
        A[u].sz = 1;
        for (int v : g[u]) {
            if (v == fa) continue;
            dfs1(v, u);
            A[u].sz += A[v].sz;
            if (A[u].son == 0 || A[A[u].son].sz < A[v].sz) A[u].son = v;
        }
        return;
    };
    dfs1(0, -1);

    int dfn = 0;
    auto dfs2 = [&](this auto&& dfs2, int u, int top) -> void {
        if (u == -1) return;
        A[u].top = top;
        A[u].dfn = dfn++;
        dfs2(A[u].son, top);  // 先遍歷重鏈
        for (int v : g[u]) {
            if (v == A[u].fa || v == A[u].son) continue;
            dfs2(v, v);
        }
        return;
    };
    dfs2(0, 0);

    SegmentTree<int> seg(N);
    
    auto install = [&](int x) -> int {
        int cnt1 = seg.query();
        while (A[x].top != A[0].top) {
            seg.update(A[A[x].top].dfn, A[x].dfn, 1);
            x = A[A[x].top].fa;
        }
        seg.update(0, A[x].dfn, 1);
        int cnt2 = seg.query();
        return abs(cnt2 - cnt1);
    };

    auto uninstall = [&](int x) -> int {
        int cnt1 = seg.query();
        seg.update(A[x].dfn, A[x].dfn + A[x].sz - 1, 0);
        int cnt2 = seg.query();
        return abs(cnt2 - cnt1);
    };

    cin >> M;
    string op;
    int x;
    while (M--) {
        cin >> op >> x;
        if (op == "install") cout << install(x) << endl;
        else cout << uninstall(x) << endl;
    }
    return 0;
}