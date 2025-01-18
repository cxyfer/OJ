#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

/*
    可持久化線段樹
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
    int n;
    vector<T> A;
    vector<SegNode<T>*> roots; // 維護每個版本的根節點

    SegmentTree(vector<T> &A) : A(A) {
        this->n = A.size();
        roots.push_back(build(1, n, A));
    }

    // 根据 A 陣列建立線段樹，返回根節點
    SegNode<T>* build(int left, int right, vector<T> &A) {
        SegNode<T> *node = new SegNode<T>();
        if (left == right) {
            node->val = A[left - 1]; // 注意下標
            return node;
        }
        // int mid = left + ((right - left) >> 1);
        int mid = (left + right) >> 1;
        node->ls = build(left, mid, A);
        node->rs = build(mid + 1, right, A);
        return node;
    }

    // 在 [left, right] 區間內，尋找並更新 idx 位置的值為 v，返回新的根節點
    SegNode<T>* update(SegNode<T> *prev, int left, int right, int idx, T v) {
        SegNode<T> *node = new SegNode<T>();
        *node = *prev;
        if (left == right) {
            node->val = v;
            return node;
        }
        // int mid = left + ((right - left) >> 1);
        int mid = (left + right) >> 1;
        if (idx <= mid) {
            node->ls = update(prev->ls, left, mid, idx, v);
        } else {
            node->rs = update(prev->rs, mid + 1, right, idx, v);
        }
        return node;
    }

    // 在 [left, right] 區間內，尋找 idx 位置的值
    T query(SegNode<T> *node, int left, int right, int idx) {
        if (left == right) return node->val;
        int mid = left + ((right - left) >> 1);
        if (idx <= mid) return query(node->ls, left, mid, idx);
        else return query(node->rs, mid + 1, right, idx);
    }
};

inline int read() {
    int x = 0, f = 1;
    char c = getchar();
    while (c < '0' || c > '9') {
        if (c == '-') f = -1;
        c = getchar();
    }
    while (c >= '0' && c <= '9') {
        x = (x << 3) + (x << 1) + (c ^ 48);
        c = getchar();
    }
    return x * f;
}
inline void write(int x) {
    if (x < 0) {
        putchar('-');
        x = -x;
    }
    if (x > 9) write(x / 10);
    putchar(x % 10 + '0');
}

int main() {
    int n = read(), q = read();
    vector<int> A(n);
    for (int i = 0; i < n; i++) A[i] = read();
    SegmentTree<int> seg(A);
    int v, op, idx, val;
    while (q--) {
        v = read(), op = read();
        if (op == 1) {
            idx = read(), val = read();
            seg.roots.push_back(seg.update(seg.roots[v], 1, seg.n, idx, val));
        } else {
            idx = read();
            write(seg.query(seg.roots[v], 1, seg.n, idx));
            putchar('\n');
            seg.roots.push_back(seg.roots[v]);
        }
    }
    return 0;
}