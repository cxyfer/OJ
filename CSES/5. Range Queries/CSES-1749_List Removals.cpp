#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

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
        // Calculate answer: sum of range
        int ans = 0;
        if (l <= mid) ans = query(node->ls, left, mid, l, r);
        if (r > mid) ans += query(node->rs, mid + 1, right, l, r);
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
        // Update method: sum of range
        node->val = node->ls->val + node->rs->val;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, q, left, right;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    SegmentTree *st = new SegmentTree();
    for (int i = 0; i < n; i++) st->update(st->root, 0, n - 1, i, i, 1);
    for (int i = 0; i < n; i++) {
        cin >> q;
        left = 0, right = n;
        while (left <= right) {
            int mid = left + ((right - left) >> 1);
            if (st->query(st->root, 0, n - 1, 0, mid) >= q) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        cout << nums[left] << " ";
        st->update(st->root, 0, n - 1, left, left, -1);
    }
    cout << endl;
    return 0;
}