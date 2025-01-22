#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

struct Node {
    LL z, p, s;
    bool a;
    Node(LL z = 0, LL p = 0, LL s = 0, bool a = false) 
        : z(z), p(p), s(s), a(a) {}
};

class SegmentTree {
public:
    int n;
    string s;
    vector<Node> tree;

    SegmentTree(const string& str) {
        s = "#" + str;
        n = str.length();
        tree.resize(4 * n);
        build(1, 1, n);
    }

    void build(int o, int left, int right) {
        if (left == right) {
            tree[o] = (s[left] == '0') ? Node(1, 1, 1, true) : Node(0, 0, 0, false);
            return;
        }
        int mid = (left + right) >> 1;
        build(2*o, left, mid);
        build(2*o+1, mid + 1, right);
        tree[o] = merge(tree[2 * o], tree[2 * o + 1], left, mid, right);
    }

    Node merge(const Node& left_part, const Node& right_part, int left, int mid, int right) {
        bool a = (left_part.a && right_part.a);
        LL p = left_part.a ? (mid - left + 1) + right_part.p : left_part.p;
        LL s = right_part.a ? (right - mid) + left_part.s : right_part.s;
        LL z = left_part.z + right_part.z + left_part.s * right_part.p;
        return Node(z, p, s, a);
    }

    Node query(int o, int left, int right, int l, int r) {
        if (left == l && right == r) return tree[o];
        int mid = (left + right) >> 1;
        if (r <= mid) return query(2*o, left, mid, l, r);
        if (mid < l) return query(2*o+1, mid + 1, right, l, r);
        Node left_part = query(2*o, left, mid, l, mid);
        Node right_part = query(2*o+1, mid + 1, right, mid + 1, r);
        return merge(left_part, right_part, l, mid, r);
    }
};

LL count(LL L) {
    return L * (L + 1) / 2;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, q, l, r;
    string s;
    cin >> n >> s >> q;
    SegmentTree st(s);
    while (q--) {
        int l, r;
        cin >> l >> r;
        cout << count(r - l + 1) - st.query(1, 1, n, l, r).z << endl;
    }
    return 0;
}