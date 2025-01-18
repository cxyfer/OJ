#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

template<typename T>
struct SegNode {
    SegNode *ls, *rs; // left child, right child
    T val, lazy; // value, lazy tag
    SegNode() : ls(nullptr), rs(nullptr), val(0), lazy(0) {}
};

template<typename T>
class SegmentTree {
public:
    SegNode<T> *root;
    
    SegmentTree() {
        root = new SegNode<T>();
    }

    // Update the range [l, r] with value v
    void update(SegNode<T> *node, int left, int right, int l, int r, T v) {
        if (l <= left && right <= r) {
            // Update node value (Customized)
            _update(node, left, right, v);
            return;
        }
        pushdown(node, left, right);
        int mid = left + ((right - left) >> 1);
        if (l <= mid) update(node->ls, left, mid, l, r, v);
        if (r > mid) update(node->rs, mid + 1, right, l, r, v);
        pushup(node); // Push up node value
    }

    // Update node value (Customized)
    void _update(SegNode<T> *node, int left, int right, T v) {
        node->val = (v & 1) ? (right - left + 1) - node->val : node->val;
        node->lazy += v;
    }

    // Query the range [l, r]
    T query(SegNode<T> *node, int left, int right, int l, int r) {
        if (l <= left && right <= r) {
            return node->val;
        }
        pushdown(node, left, right);
        int mid = left + ((right - left) >> 1);
        // Calculate answer (Customized)
        T ans = 0;
        if (l <= mid) ans += query(node->ls, left, mid, l, r);
        if (r > mid) ans += query(node->rs, mid + 1, right, l, r);
        return ans;
    }

    // Push down lazy tags
    void pushdown(SegNode<T> *node, int left, int right) {
        if (node->ls == nullptr) node->ls = new SegNode<T>();
        if (node->rs == nullptr) node->rs = new SegNode<T>();
        if (node->lazy != 0) {
            int mid = left + ((right - left) >> 1);
            // Update node value (Customized)
            _update(node->ls, left, mid, node->lazy);
            _update(node->rs, mid + 1, right, node->lazy);
            node->lazy = 0;
        }
    }

    // Push up node value
    void pushup(SegNode<T> *node) {
        // Update method (Customized)
        node->val = node->ls->val + node->rs->val;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, q; cin >> n >> q;
    SegmentTree<int> seg;
    int op, l, r;
    while (q--) {
        cin >> op >> l >> r;
        if (op == 0) {
            seg.update(seg.root, 1, n, l, r, 1);
        } else {
            cout << seg.query(seg.root, 1, n, l, r) << endl;
        }
    }
    return 0;
}