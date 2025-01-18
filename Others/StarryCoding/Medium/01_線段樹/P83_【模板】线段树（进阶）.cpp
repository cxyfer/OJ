#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const LL MOD = 998244353;
#define endl '\n'

/*
    Operation 1: val * 1 + v 
    Operation 2: val * k + 0
    Operation 3: val * 0 + v
*/

LL mod(LL x) {
    return (x % MOD + MOD) % MOD;
}

template<typename T>
struct SegNode {
    SegNode *ls, *rs; // left child, right child
    T val, mul, add; // value, lazy tag
    SegNode() : ls(nullptr), rs(nullptr), val(0), mul(1), add(0) {}
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
            node->val = mod(nums[left - 1]); // assert nums is 0-indexed
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
    void update(SegNode<T> *node, int left, int right, int l, int r, T k, T v) {
        if (l <= left && right <= r) {
            // Update node value (Customized)
            _update(node, left, right, k, v);
            return;
        }
        pushdown(node, left, right);
        int mid = left + ((right - left) >> 1);
        if (l <= mid) update(node->ls, left, mid, l, r, k, v);
        if (r > mid) update(node->rs, mid + 1, right, l, r, k, v);
        pushup(node); // Push up node value
    }

    // Update node value (Customized)
    void _update(SegNode<T> *node, int left, int right, T k, T v) {
        /*
            實際值 rv = val * mul + add
            rv * k + v
            = (val * mul + add) * k + v
            = val * (mul * k) + (add * k + v)
            = val * mul' + add'
        */
        node->val = mod(k * node->val + v * (right - left + 1));
        node->mul = mod(k * node->mul);
        node->add = mod(mod(k * node->add) + v);
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
        return mod(ans);
    }

    // Push down lazy tags
    void pushdown(SegNode<T> *node, int left, int right) {
        if (node->ls == nullptr) node->ls = new SegNode<T>();
        if (node->rs == nullptr) node->rs = new SegNode<T>();
        if (node->mul != 1 || node->add != 0) {
            // Update node value (Customized)
            int mid = left + ((right - left) >> 1);
            _update(node->ls, left, mid, node->mul, node->add);
            _update(node->rs, mid + 1, right, node->mul, node->add);
            node->mul = 1;
            node->add = 0;
        }
    }

    // Push up node value
    void pushup(SegNode<T> *node) {
        // Update method (Customized)
        node->val = mod(node->ls->val + node->rs->val);
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
            seg.update(seg.root, 1, n, l, r, 1, v);
        } else if (op == 2) {
            cin >> l >> r >> v;
            seg.update(seg.root, 1, n, l, r, v, 0);
        } else if (op == 3) {
            cin >> l >> r >> v;
            seg.update(seg.root, 1, n, l, r, 0, v);
        } else {
            cin >> l >> r;
            cout << seg.query(seg.root, 1, n, l, r) << endl;
        }
    }
    return 0;
}