#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

template<typename T>
struct SegNode {
    SegNode *ls, *rs; // left child, right child
    T val, lazy_k, lazy_d; // value, lazy tag
    SegNode() : ls(nullptr), rs(nullptr), val(0), lazy_k(0), lazy_d(0) {}
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
            node->val = nums[left - 1]; // assert nums is 0-indexed
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
    void update(SegNode<T> *node, int left, int right, int l, int r, T k, T d) {
        if (l <= left && right <= r) {
            // Update node value (Customized)
            // 這個區間的首項是 k + d * (left - l)，公差是 d
            _update(node, left, right, k + d * (left - l), d);
            return;
        }
        pushdown(node, left, right);
        int mid = left + ((right - left) >> 1);
        if (l <= mid) update(node->ls, left, mid, l, r, k, d);
        if (r > mid) update(node->rs, mid + 1, right, l, r, k, d);
        pushup(node); // Push up node value
    }

    // Update node value (Customized)
    void _update(SegNode<T> *node, int left, int right, T k, T d) {
        /*
        k + (k + d) + (k + 2d) + ... + (k + (right - left) * d)
        = (right - left + 1) * k + d * (0 + 1 + 2 + ... + (right - left))
        = (right - left + 1) * k + d * (right - left) * (right - left + 1) / 2
        */
        node->val += k * (right - left + 1) + d * (right - left) * (right - left + 1) / 2;
        node->lazy_k += k;
        node->lazy_d += d;
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
        if (node->lazy_k != 0 || node->lazy_d != 0) {
            // Update node value (Customized)
            int mid = left + ((right - left) >> 1);
            // 左區間的首項 k 和公差 d 不變
            _update(node->ls, left, mid, node->lazy_k, node->lazy_d);
            // 右區間的公差 d 不變、首項 k = k + d * ln，其中 ln = mid - left + 1 為左區間的長度
            _update(node->rs, mid + 1, right, node->lazy_k + node->lazy_d * (mid - left + 1), node->lazy_d);
            node->lazy_k = 0;
            node->lazy_d = 0;
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
    vector<LL> nums(n);
    for (int i = 0; i < n; ++i) cin >> nums[i];
    SegmentTree<LL> seg(nums);
    int op, l, r, k, d, p;
    while (q--) {
        cin >> op;
        if (op == 1) {
            cin >> l >> r >> k >> d;
            seg.update(seg.root, 1, n, l, r, k, d);
        } else {
            cin >> p;
            cout << seg.query(seg.root, 1, n, p, p) << endl;
        }
    }
    return 0;
}