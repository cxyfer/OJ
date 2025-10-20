#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const LL INF = LLONG_MAX;
#define endl '\n'

/*
    Lazy Segment Tree
*/

template<typename T>
struct SegNode {
    SegNode *ls, *rs; // left child, right child
    T mn, cnt, lazy; // minimum value, count of non-zero elements, lazy tag
    SegNode() : ls(nullptr), rs(nullptr), mn(0), cnt(0), lazy(0) {}
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
            node->mn = nums[left - 1];
            node->cnt = nums[left - 1] != 0 ? 1 : 0;  // assert nums is 0-indexed
            return;
        }
        int mid = left + ((right - left) >> 1);
        node->ls = new SegNode<T>();
        node->rs = new SegNode<T>();
        build(node->ls, left, mid, nums);
        build(node->rs, mid + 1, right, nums);
        pushup(node);  // Push up node value
    }

    // Update node value (Customized)
    void _update(SegNode<T> *node, int left, int right, T v) {
        if (node->cnt == 0) return;
        node->mn += v;
        node->lazy += v;
        return;
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
        node->mn = min(node->ls->mn, node->rs->mn);
        node->cnt = node->ls->cnt + node->rs->cnt;
    }

    // Query the range [l, r]
    T query(SegNode<T> *node, int left, int right, int l, int r, T k) {
        if (node->cnt == 0) return 0;
        if (l <= left && right <= r && node->mn > k) {
            _update(node, left, right, -k);
            return k * node->cnt;
        }
        if (left == right) {
            T res = node->mn;
            node->cnt = node->lazy = 0;
            node->mn = INF;
            return res;
        }
        pushdown(node, left, right);
        int mid = left + ((right - left) >> 1);
        T ans = 0;
        if (l <= mid) ans += query(node->ls, left, mid, l, r, k);
        if (r > mid) ans += query(node->rs, mid + 1, right, l, r, k);
        pushup(node);
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, q, l, r, k;
    cin >> n;
    vector<LL> nums(n);
    for (auto &x : nums) cin >> x;
    SegmentTree<LL> seg(nums);
    cin >> q;
    while (q--) {
        cin >> l >> r >> k;
        cout << seg.query(seg.root, 1, n, l, r, k) << endl;
    }
    return 0;
}