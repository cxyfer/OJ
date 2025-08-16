/*
 * P3372 【模板】线段树 1
 * https://www.luogu.com.cn/problem/P3372
 */
#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

template<typename T>
struct SegInfo {
    T s;
    SegInfo() : s(0) {}
    SegInfo(T s) : s(s) {}

    SegInfo operator+(SegInfo const& other) const {
        return SegInfo(s + other.s);
    }

    SegInfo operator+=(SegInfo const& other) {
        s += other.s;
        return *this;
    }
};

template<typename T>
struct SegNode {
    SegNode *ls, *rs; // left child, right child
    SegInfo<T> val; // value
    T lazy; // lazy tag
    SegNode() : ls(nullptr), rs(nullptr), val(0), lazy(0) {}
};

template<typename T>
class SegmentTree {
public:
    SegmentTree(vector<T>& nums) {
        n = nums.size() - 1;
        root = new SegNode<T>();
        build(root, 1, n, nums);
    }

    void update(int l, int r, T v) {
        _update(root, 1, n, l, r, v);
    }

    SegInfo<T> query(int l, int r) {
        return _query(root, 1, n, l, r);
    }

private:
    int n;
    SegNode<T>* root;
    void build(SegNode<T>* node, int left, int right, vector<T>& nums) {
        if (left == right) {
            node->val = SegInfo<T>(nums[left]);
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
            apply(node, left, right, v);
            return;
        }
        pushdown(node, left, right);
        int mid = left + ((right - left) >> 1);
        if (l <= mid) _update(node->ls, left, mid, l, r, v);
        if (r > mid) _update(node->rs, mid + 1, right, l, r, v);
        pushup(node);  // Push up node value
    }

    // Update node value (Customized)
    void apply(SegNode<T>* node, int left, int right, T v) {
        node->val.s += v * (right - left + 1);
        node->lazy += v;
    }

    // Query the range [l, r]
    SegInfo<T> _query(SegNode<T>* node, int left, int right, int l, int r) {
        if (l <= left && right <= r) {
            return node->val;
        }
        pushdown(node, left, right);
        int mid = left + ((right - left) >> 1);
        // Calculate answer (Customized)
        SegInfo<T> ans = SegInfo<T>();
        if (l <= mid) ans = ans + _query(node->ls, left, mid, l, r);
        if (r > mid) ans = ans + _query(node->rs, mid + 1, right, l, r);
        return ans;
    }

    // Push down lazy tags
    void pushdown(SegNode<T>* node, int left, int right) {
        if (node->ls == nullptr) node->ls = new SegNode<T>();
        if (node->rs == nullptr) node->rs = new SegNode<T>();
        if (node->lazy != 0) {
            int mid = left + ((right - left) >> 1);
            // Update node value (Customized)
            apply(node->ls, left, mid, node->lazy);
            apply(node->rs, mid + 1, right, node->lazy);
            node->lazy = 0;
        }
    }

    // Push up node value
    void pushup(SegNode<T>* node) {
        // Update method (Customized)
        node->val = node->ls->val + node->rs->val;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, q; cin >> n >> q;
    vector<LL> nums(n + 1);
    for (int i = 1; i <= n; ++i) cin >> nums[i];
    SegmentTree<LL> seg(nums);
    int op; LL l, r, v;
    while (q--) {
        cin >> op;
        if (op == 1) {
            cin >> l >> r >> v;
            seg.update(l, r, v);
        } else {
            cin >> l >> r;
            cout << seg.query(l, r).s << endl;
        }
    }
    return 0;
}