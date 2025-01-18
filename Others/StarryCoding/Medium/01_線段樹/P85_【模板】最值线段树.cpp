#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const LL INF = 0x3f3f3f3f3f3f3f3f;
#define endl '\n'

template<typename T>
struct SegNode {
    SegNode *ls, *rs; // left child, right child
    T mx, mn, lazy; // value, lazy tag
    SegNode() : ls(nullptr), rs(nullptr), mx(0), mn(0), lazy(0) {}
};

template<typename T>
class SegmentTree {
public:
    SegNode<T> *root;
    
    SegmentTree() {
        root = new SegNode<T>();
    }

    SegmentTree(vector<T> &nums) {
        root = new SegNode<T>();
        build(root, 1, nums.size(), nums);
    }

    void build(SegNode<T> *node, int left, int right, vector<T> &nums) {
        if (left == right) {
            node->mx = nums[left - 1]; // assert nums is 0-indexed
            node->mn = nums[left - 1]; // assert nums is 0-indexed
            return;
        }
        int mid = left + ((right - left) >> 1);
        node->ls = new SegNode<T>();
        node->rs = new SegNode<T>();
        build(node->ls, left, mid, nums);
        build(node->rs, mid + 1, right, nums);
        pushup(node); // Push up node value
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
        node->mx += v;
        node->mn += v;
        node->lazy += v;
    }

    // Query the range [l, r]
    T query_mx(SegNode<T> *node, int left, int right, int l, int r) {
        if (l <= left && right <= r) {
            return node->mx;
        }
        pushdown(node, left, right);
        int mid = left + ((right - left) >> 1);
        // Calculate answer (Customized)
        T ans = -INF;
        if (l <= mid) ans = max(ans, query_mx(node->ls, left, mid, l, r));
        if (r > mid) ans = max(ans, query_mx(node->rs, mid + 1, right, l, r));
        return ans;
    }

    T query_mn(SegNode<T> *node, int left, int right, int l, int r) {
        if (l <= left && right <= r) {
            return node->mn;
        }
        pushdown(node, left, right);
        int mid = left + ((right - left) >> 1);
        // Calculate answer (Customized)
        T ans = INF;
        if (l <= mid) ans = min(ans, query_mn(node->ls, left, mid, l, r));
        if (r > mid) ans = min(ans, query_mn(node->rs, mid + 1, right, l, r));
        return ans;
    }

    // Push down lazy tags
    void pushdown(SegNode<T> *node, int left, int right) {
        if (node->ls == nullptr) node->ls = new SegNode<T>();
        if (node->rs == nullptr) node->rs = new SegNode<T>();
        if (node->lazy != 0) {
            // Update node value (Customized)
            int mid = left + ((right - left) >> 1);
            _update(node->ls, left, mid, node->lazy);
            _update(node->rs, mid + 1, right, node->lazy);
            node->lazy = 0;
        }
    }

    // Push up node value
    void pushup(SegNode<T> *node) {
        // Update method (Customized)
        node->mx = max(node->ls->mx, node->rs->mx);
        node->mn = min(node->ls->mn, node->rs->mn);
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, q; cin >> n >> q;
    vector<LL> nums(n);
    for (int i = 0; i < n; ++i) cin >> nums[i];
    SegmentTree<LL> seg(nums);
    int op, l, r, v;
    while (q--) {
        cin >> op;
        if (op == 1) {
            cin >> l >> r >> v;
            seg.update(seg.root, 1, n, l, r, v);
        } else {
            cin >> l >> r;
            cout << seg.query_mx(seg.root, 1, n, l, r) << ' ' << seg.query_mn(seg.root, 1, n, l, r) << endl;
        }
    }
    return 0;
}