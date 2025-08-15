/*
 * P3384 【模板】重链剖分/树链剖分
 * https://www.luogu.com.cn/problem/P3384
 */
#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

struct Node {
    int val, fa, dep, sz, son, top, dfn;
    Node() : val(0), fa(0), dep(0), sz(0), son(0), top(0), dfn(0) {}
};

template <typename T>
struct SegNode {
    SegNode *ls, *rs;  // left child, right child
    T val, lazy;       // value, lazy tag
    SegNode() : ls(nullptr), rs(nullptr), val(0), lazy(0) {}
};

template <typename T>
class SegmentTree {
public:
    SegmentTree(int n, int MOD) : n(n), MOD(MOD) {
        root = new SegNode<T>();
    }

    SegmentTree(vector<T>& nums, int MOD) : MOD(MOD) {
        n = nums.size() - 1;
        root = new SegNode<T>();
        build(root, 1, n, nums);
    }

    void update(int l, int r, T v) {
        _update(root, 1, n, l, r, v);
    }

    T query(int l, int r) {
        return _query(root, 1, n, l, r);
    }

private:
    int n, MOD;
    SegNode<T>* root;
    void build(SegNode<T>* node, int left, int right, vector<T>& nums) {
        if (left == right) {
            node->val = nums[left] % MOD;
            return;
        }
        int mid = left + ((right - left) >> 1);
        node->ls = new SegNode<T>();
        node->rs = new SegNode<T>();
        build(node->ls, left, mid, nums);
        build(node->rs, mid + 1, right, nums);
        pushup(node);  // Push up node value
    }

    // Update the range [l, r] with value v
    void _update(SegNode<T>* node, int left, int right, int l, int r, T v) {
        if (l <= left && right <= r) {
            // Update node value (Customized)
            __update(node, left, right, v);
            return;
        }
        pushdown(node, left, right);
        int mid = left + ((right - left) >> 1);
        if (l <= mid) _update(node->ls, left, mid, l, r, v);
        if (r > mid) _update(node->rs, mid + 1, right, l, r, v);
        pushup(node);  // Push up node value
    }

    // Update node value (Customized)
    void __update(SegNode<T>* node, int left, int right, T v) {
        node->val = (node->val + 1LL * v * (right - left + 1) % MOD) % MOD;
        node->lazy = (node->lazy + v) % MOD;
    }

    // Query the range [l, r]
    T _query(SegNode<T>* node, int left, int right, int l, int r) {
        if (l <= left && right <= r) {
            return node->val;
        }
        pushdown(node, left, right);
        int mid = left + ((right - left) >> 1);
        // Calculate answer (Customized)
        T ans = 0;
        if (l <= mid) ans += _query(node->ls, left, mid, l, r);
        if (r > mid) ans += _query(node->rs, mid + 1, right, l, r);
        return ans % MOD;
    }

    // Push down lazy tags
    void pushdown(SegNode<T>* node, int left, int right) {
        if (node->ls == nullptr) node->ls = new SegNode<T>();
        if (node->rs == nullptr) node->rs = new SegNode<T>();
        if (node->lazy != 0) {
            int mid = left + ((right - left) >> 1);
            // Update node value (Customized)
            __update(node->ls, left, mid, node->lazy);
            __update(node->rs, mid + 1, right, node->lazy);
            node->lazy = 0;
        }
    }

    // Push up node value
    void pushup(SegNode<T>* node) {
        // Update method (Customized)
        node->val = (node->ls->val + node->rs->val) % MOD;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int N, M, R, MOD;
    cin >> N >> M >> R >> MOD;

    vector<Node> A(N + 1);
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
    SegmentTree<int> seg(vals, MOD);

    auto pathAdd = [&](int x, int y, int v) -> void {
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
    };

    auto pathSum = [&](int x, int y) -> int {
        int ans = 0;
        while (A[x].top != A[y].top) {
            if (A[A[x].top].dep >= A[A[y].top].dep) {
                ans = (ans + seg.query(A[A[x].top].dfn, A[x].dfn)) % MOD;
                x = A[A[x].top].fa;
            } else {
                ans = (ans + seg.query(A[A[y].top].dfn, A[y].dfn)) % MOD;
                y = A[A[y].top].fa;
            }
        }
        int l = min(A[x].dfn, A[y].dfn), r = max(A[x].dfn, A[y].dfn);
        ans = (ans + seg.query(l, r)) % MOD;
        return ans;
    };

    int op, x, y, v;
    while (M--) {
        cin >> op;
        if (op == 1) {
            cin >> x >> y >> v;
            pathAdd(x, y, v);
        } else if (op == 2) {
            cin >> x >> y;
            cout << pathSum(x, y) << endl;
        } else if (op == 3) {
            cin >> x >> v;
            seg.update(A[x].dfn, A[x].dfn + A[x].sz - 1, v);
        } else {
            cin >> x;
            cout << seg.query(A[x].dfn, A[x].dfn + A[x].sz - 1) << endl;
        }
    }
    return 0;
}