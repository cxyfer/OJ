#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
/*
    Lazy Segment Tree
    - 動態開點，只有當需要用到子節點時，才會創建子節點

    Problem:
    - 731. My Calendar II
    - 732. My Calendar III
*/

struct SegNode {
    SegNode *ls, *rs; // left child, right child
    int val, lazy; // value, lazy tag
    SegNode() : ls(nullptr), rs(nullptr), val(0), lazy(0) {}
};

class SegmentTree {
public:
    SegNode *root;
    
    SegmentTree() {
        root = new SegNode();
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
    int query(SegNode *node, int left, int right, int l, int r) {
        if (l <= left && right <= r) {
            return node->val;
        }
        // Ensure all lazy tags have been pushed down
        pushdown(node);
        int mid = left + ((right - left) >> 1);
        // Calculate answer
        int ans = 0;
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
        // Update method
        node->val = node->ls->val + node->rs->val;
    }
};



int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, q; cin >> n >> q;
    int op, l, r, v;
    SegmentTree seg;
    while (q--) {
        cin >> op;
        if (op == 1) {
            cin >> l >> r >> v;
            seg.update(seg.root, 1, n, l, r, v);
        } else {
            cin >> l >> r;
            cout << seg.query(seg.root, 1, n, l, r) << endl;
    }
    return 0;
}