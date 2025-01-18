#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int N = 2e5 + 5;
#define endl '\n'

template<typename T>
struct SegNode {
    SegNode *ls, *rs; // left child, right child
    T val; // value
    SegNode() : ls(nullptr), rs(nullptr), val(0) {}
};

template<typename T>
class SegmentTree {
public:
    SegNode<T> *root;
    
    SegmentTree() {
        root = new SegNode<T>();
    }

    void insert(SegNode<T> *node, int left, int right, T v) {
        if (left == right) {
            node->val++;
            return;
        }
        int mid = left + ((right - left) >> 1);
        if (v <= mid) {
            if (node->ls == nullptr) node->ls = new SegNode<T>();
            insert(node->ls, left, mid, v);
        } else {
            if (node->rs == nullptr) node->rs = new SegNode<T>();
            insert(node->rs, mid + 1, right, v);
        }
        pushup(node);
    }

    // Push up node value
    void pushup(SegNode<T> *node) {
        // Update method (Customized)
        node->val = 0;
        if (node->ls) node->val += node->ls->val;
        if (node->rs) node->val += node->rs->val;
    }

    // Query the range [l, r]
    T query(SegNode<T> *node, int left, int right, int l, int r) {
        if (node == nullptr) return 0;
        if (l <= left && right <= r) {
            return node->val;
        }
        int mid = left + ((right - left) >> 1);
        // Calculate answer (Customized)
        T ans = 0;
        if (l <= mid && node->ls) ans += query(node->ls, left, mid, l, r);
        if (r > mid && node->rs) ans += query(node->rs, mid + 1, right, l, r);
        return ans;
    }

    // Query the k-th smallest element
    T queryKth(SegNode<T> *node, int left, int right, int k) {
        if (left == right) return left;
        int mid = left + ((right - left) >> 1);
        int leftCnt = node->ls ? node->ls->val : 0;
        if (k <= leftCnt && node->ls) return queryKth(node->ls, left, mid, k);
        else if (node->rs) return queryKth(node->rs, mid + 1, right, k - leftCnt);
        return -1;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int q; cin >> q;
    SegmentTree<LL> seg;
    int op, x, l, r, k;
    while (q--) {
        cin >> op;
        if (op == 1) {
            cin >> x;
            seg.insert(seg.root, 1, N, x);
        } else if (op == 2) {
            cin >> l >> r;
            cout << seg.query(seg.root, 1, N, l, r) << endl;
        } else {
            cin >> k;
            cout << seg.queryKth(seg.root, 1, N, k) << endl;
        }
    }
    return 0;
}