#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

/*
    離散化
*/
class Discrete {
public:
    vector<int> A;
    Discrete(vector<int> A) {
        sort(A.begin(), A.end()); // 排序
        A.erase(unique(A.begin(), A.end()), A.end()); // 去重
        this->A = A;
    }
    
    int get(int x, int start = 1) {
        return lower_bound(A.begin(), A.end(), x) - A.begin() + start;
    }
};

/*
    可持久化權值線段樹
*/

template<typename T>
struct SegNode {
    SegNode *ls, *rs; // left child, right child
    T val; // value
    SegNode() : ls(nullptr), rs(nullptr), val(0) {}
};

template<typename T>
class SegmentTree {
public:
    int n; // 離散化後的大小
    vector<T> A;
    Discrete d;
    vector<SegNode<T>*> roots;

    SegmentTree(vector<T> &A) : d(A) {
        this->n = d.A.size();
        this->A = A;
        roots.push_back(new SegNode<T>());
        build();
    }

    void build() {
        for (int i = 0; i < A.size(); i++) {
            roots.push_back(insert(roots.back(), 1, n, d.get(A[i])));
        }
    }

    // 在區間 [left, right] 插入值 v，返回新的根節點
    SegNode<T>* insert(SegNode<T> *prev, int left, int right, T v) {
        SegNode<T> *node = new SegNode<T>();
        *node = *prev; // 複製舊的節點
        
        if (left == right) {
            node->val++;
            return node;
        }
        
        int mid = left + ((right - left) >> 1);
        if (v <= mid) {
            if (!prev->ls) prev->ls = new SegNode<T>();
            node->ls = insert(prev->ls, left, mid, v);
        } else {
            if (!prev->rs) prev->rs = new SegNode<T>();
            node->rs = insert(prev->rs, mid + 1, right, v);
        }
        pushup(node);
        return node;
    }

    // Push up node value
    void pushup(SegNode<T> *node) {
        // Update method (Customized)
        node->val = 0;
        if (node->ls) node->val += node->ls->val;
        if (node->rs) node->val += node->rs->val;
    }

    // Query the k-th smallest element
    T queryKth(SegNode<T> *node, SegNode<T> *prev, int left, int right, int k) {
        if (left == right) return left;
        int mid = left + ((right - left) >> 1);
        int leftCnt = (node->ls ? node->ls->val : 0) - (prev->ls ? prev->ls->val : 0);
        if (prev->ls == nullptr) prev->ls = new SegNode<T>();
        if (prev->rs == nullptr) prev->rs = new SegNode<T>();
        if (k <= leftCnt) {
            return queryKth(node->ls, prev->ls, left, mid, k);
        } else {
            return queryKth(node->rs, prev->rs, mid + 1, right, k - leftCnt);
        }
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, q; cin >> n >> q;
    vector<int> A(n);
    for (int i = 0; i < n; i++) cin >> A[i];
    SegmentTree<int> seg(A);
    int l, r, k;
    while (q--) {
        cin >> l >> r >> k;
        int pos = seg.queryKth(seg.roots[r], seg.roots[l - 1], 1, seg.n, k);
        cout << seg.d.A[pos - 1] << endl;
    }
    return 0;
}