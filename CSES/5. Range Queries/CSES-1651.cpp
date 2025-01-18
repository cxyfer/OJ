#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

struct SegNode {
    SegNode *ls, *rs; // left child, right child
    LL val, lazy; // value, lazy tag
    SegNode() : ls(nullptr), rs(nullptr), val(0), lazy(0) {}
};

class SegmentTree {
public:
    SegNode *root;
    vector<LL> arr;
    
    SegmentTree() {
        root = new SegNode();
    }

    SegmentTree(vector<LL> &arr) {
        this->arr = arr;
        root = build(0, arr.size() - 1);
    }

    // Build the segment tree
    SegNode* build(int left, int right) {
        SegNode *node = new SegNode();
        if (left == right) {
            node->val = arr[left];
            return node;
        }
        int mid = left + ((right - left) >> 1);
        node->ls = build(left, mid);
        node->rs = build(mid + 1, right);
        pushup(node);
        return node;
    }

    // Update the range [l, r] with value v
    void update(SegNode *node, int left, int right, int l, int r, int v) {
        if (l <= left && right <= r) {
            node->lazy += v;
            node->val += v;
            return;
        }
        pushdown(node); // Push down lazy tags
        int mid = left + ((right - left) >> 1);
        if (l <= mid) update(node->ls, left, mid, l, r, v);
        if (r > mid) update(node->rs, mid + 1, right, l, r, v);
        pushup(node); // Push up node value
    }

    // Query the range [l, r]
    LL query(SegNode *node, int left, int right, int l, int r) {
        if (l <= left && right <= r) {
            return node->val;
        }
        // Ensure all lazy tags have been pushed down
        pushdown(node);
        int mid = left + ((right - left) >> 1);
        // Calculate answer: maximum value in this problem
        LL ans = 0;
        if (l <= mid) ans = query(node->ls, left, mid, l, r);
        if (r > mid) ans = max(ans, query(node->rs, mid + 1, right, l, r));
        return ans;
    }

    // Push down lazy tags
    void pushdown(SegNode *node) {
        if (node->ls == nullptr) node->ls = new SegNode();
        if (node->rs == nullptr) node->rs = new SegNode();
        if (node->lazy != 0) {
            node->ls->lazy += node->lazy;
            node->rs->lazy += node->lazy;
            node->ls->val += node->lazy;
            node->rs->val += node->lazy;
            node->lazy = 0; // Clear current node's lazy tag
        }
    }

    // Push up node value
    void pushup(SegNode *node) {
        // Update method: maximum value in this problem
        node->val = max(node->ls->val, node->rs->val);
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, q, t, a, b, u, k;
    cin >> n >> q;
    vector<LL> arr(n);
    for (int i = 0; i < n; ++i) cin >> arr[i];
    SegmentTree st(arr);
    while (q--) {
        cin >> t;
        if (t == 1) {
            cin >> a >> b >> u;
            st.update(st.root, 0, n - 1, a - 1, b - 1, u);
        } else {
            cin >> k;
            cout << st.query(st.root, 0, n - 1, k - 1, k - 1) << endl;
        }
    }
    return 0;
}