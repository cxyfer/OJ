/*
 * P2590 [ZJOI2008] 树的统计
 * https://www.luogu.com.cn/problem/P2590
 * 樹鏈剖分 + 線段樹
 */
#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f;
#define endl '\n'

struct Node {
    int val, fa, dep, sz, son, top, dfn;
    Node() : val(0), fa(0), dep(0), sz(0), son(0), top(0), dfn(0) {}
};

struct SegNode {
    int s, mx;
    SegNode(int s = 0, int mx = -INF) : s(s), mx(mx) {}

    SegNode operator+(SegNode const& other) const {
        return SegNode(s + other.s, max(mx, other.mx));
    }

    SegNode& operator+=(SegNode const& other) {
        s += other.s;
        mx = max(mx, other.mx);
        return *this;
    }
};

class SegmentTree {
public:
    SegmentTree(vector<int>& nums) {
        this->n = nums.size() - 1;
        this->tree = vector<SegNode>(4 * n, SegNode(0, 0));
        build(1, 1, n, nums);
    }

    void update(int idx, int val) {
        _update(1, 1, n, idx, val);
    }

    SegNode query(int l, int r) {
        return _query(1, 1, n, l, r);
    }

private:
    int n;
    vector<SegNode> tree;

    void build(int o, int left, int right, vector<int>& nums) {
        if (left == right) {
            tree[o].s = nums[left];
            tree[o].mx = nums[left];
            return;
        }
        int mid = left + ((right - left) >> 1);
        build(o << 1, left, mid, nums);
        build(o << 1 | 1, mid + 1, right, nums);
        pushup(o);
    }

    // Push up node value
    void pushup(int o) {
        tree[o].s = tree[o << 1].s + tree[o << 1 | 1].s;
        tree[o].mx = max(tree[o << 1].mx, tree[o << 1 | 1].mx);
    }

    void _update(int o, int left, int right, int idx, int val) {
        if (left == right) {
            tree[o].s = val;
            tree[o].mx = val;
            return;
        }
        int mid = left + ((right - left) >> 1);
        if (idx <= mid)
            _update(o << 1, left, mid, idx, val);
        else
            _update(o << 1 | 1, mid + 1, right, idx, val);
        pushup(o);
    }

    SegNode _query(int o, int left, int right, int l, int r) {
        if (left == l && r == right) return tree[o];
        int mid = left + ((right - left) >> 1);
        if (r <= mid) return _query(o << 1, left, mid, l, r);
        if (mid < l) return _query(o << 1 | 1, mid + 1, right, l, r);
        return _query(o << 1, left, mid, l, mid) +
               _query(o << 1 | 1, mid + 1, right, mid + 1, r);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    int N, M;
    cin >> N;

    vector<Node> A(N + 1);
    vector<vector<int>> g(N + 1);
    for (int i = 1; i < N; i++) {
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }
    for (int i = 1; i <= N; i++) cin >> A[i].val;

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
    dfs1(1, 0);

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
    dfs2(1, 1);

    vector<int> vals(N + 1);
    for (int i = 1; i <= N; i++) vals[A[i].dfn] = A[i].val;
    SegmentTree seg(vals);

    auto query = [&](int x, int y) -> SegNode {
        SegNode ans;
        while (A[x].top != A[y].top) {
            if (A[A[x].top].dep >= A[A[y].top].dep) {
                ans += seg.query(A[A[x].top].dfn, A[x].dfn);
                x = A[A[x].top].fa;
            } else {
                ans += seg.query(A[A[y].top].dfn, A[y].dfn);
                y = A[A[y].top].fa;
            }
        }
        int l = min(A[x].dfn, A[y].dfn), r = max(A[x].dfn, A[y].dfn);
        ans += seg.query(l, r);
        return ans;
    };

    cin >> M;
    string op;
    int x, y, v;
    while (M--) {
        cin >> op;
        if (op == "QMAX") {
            cin >> x >> y;
            cout << query(x, y).mx << endl;
        } else if (op == "QSUM") {
            cin >> x >> y;
            cout << query(x, y).s << endl;
        } else if (op == "CHANGE") {
            cin >> x >> v;
            seg.update(A[x].dfn, v);
        }
    }
    return 0;
}