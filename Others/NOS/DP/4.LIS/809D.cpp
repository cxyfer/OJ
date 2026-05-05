#include <bits/stdc++.h>
using namespace std;
using i64 = long long;
#define endl '\n'

class FHQTreap {
public:
    class Node {
    public:
        Node *left, *right;
        int sz;
        uint32_t pri;   // Treap 的 heap priority
        i64 val, lazy;  // val: BST key, lazy: lazy tag
        Node(i64 val, uint32_t pri)
            : left(nullptr),
              right(nullptr),
              sz(1),
              pri(pri),
              val(val),
              lazy(0) {}
    };

private:
    vector<unique_ptr<Node>> pool;
    mt19937 rng;

public:
    explicit FHQTreap(int reserveNodes = 0)
        : rng(static_cast<uint32_t>(
              chrono::steady_clock::now().time_since_epoch().count())) {
        pool.reserve(reserveNodes + 5);
    }

    int size(Node* root) const {
        return root ? root->sz : 0;
    }

    // 建立一個新節點
    Node* make(i64 value) {
        pool.emplace_back(make_unique<Node>(value, rng()));
        return pool.back().get();
    }

    // 由左右子樹資訊更新目前節點
    void pushup(Node* root) {
        if (!root) return;
        root->sz = size(root->left) + size(root->right) + 1;
    }

    // 對整棵子樹套用加法標記
    void apply(Node* root, i64 value) {
        if (!root) return;
        root->val += value;
        root->lazy += value;
    }

    // 將 lazy tag 下推到左右子節點
    void pushdown(Node* root) {
        if (!root || root->lazy == 0) return;
        i64 tag = root->lazy;
        apply(root->left, tag);
        apply(root->right, tag);
        root->lazy = 0;
    }

    // 依照 key 將 Treap 分裂成兩棵
    // - a：所有 val < key 的節點
    // - b：所有 val >= key 的節點
    pair<Node*, Node*> split(Node* root, i64 key) {
        if (!root) return {nullptr, nullptr};
        pushdown(root);
        if (root->val < key) {
            auto [a, b] = split(root->right, key);
            root->right = a;
            pushup(root);
            return {root, b};
        } else {
            auto [a, b] = split(root->left, key);
            root->left = b;
            pushup(root);
            return {a, root};
        }
    }

    // 合併兩棵 Treap
    // 使用前必須保證：a 中所有值 <= b 中所有值
    Node* merge(Node* a, Node* b) {
        if (!a || !b) return a ? a : b;
        if (a->pri < b->pri) {
            pushdown(a);
            a->right = merge(a->right, b);
            pushup(a);
            return a;
        } else {
            pushdown(b);
            b->left = merge(a, b->left);
            pushup(b);
            return b;
        }
    }

    // 插入一個值
    // 若 Treap 中已存在相同值，仍會插入新節點
    Node* insert(Node* root, i64 value) {
        auto [a, b] = split(root, value);
        Node* mid = make(value);
        return merge(merge(a, mid), b);
    }

    // 刪除一個值
    // 若存在多個相同 value，只會刪除其中一個
    // 若 value 不存在，Treap 內容不變
    Node* erase(Node* root, i64 value) {
        if (!root) return nullptr;
        pushdown(root);
        if (root->val == value) return merge(root->left, root->right);
        if (value < root->val)
            root->left = erase(root->left, value);
        else
            root->right = erase(root->right, value);
        pushup(root);
        return root;
    }

    // 對所有 val 屬於 [l, r) 的節點加上 value
    // 注意：這個操作會直接修改節點的 val
    // 使用時必須確保更新後仍然不破壞 Treap 的 BST 順序
    Node* update(Node* root, i64 l, i64 r, i64 value) {
        auto [a, b] = split(root, l);
        auto [c, d] = split(b, r);
        apply(c, value);
        return merge(merge(a, c), d);
    }

    // 刪除 Treap 中的最小值
    Node* popmin(Node* root) {
        if (!root) return nullptr;
        pushdown(root);
        if (!root->left) return root->right;
        root->left = popmin(root->left);
        pushup(root);
        return root;
    }

    // 刪除 Treap 中的最大值
    Node* popmax(Node* root) {
        if (!root) return nullptr;
        pushdown(root);
        if (!root->right) return root->left;
        root->right = popmax(root->right);
        pushup(root);

        return root;
    }

    // 取得 Treap 中的最小值
    // 使用前必須保證 root != nullptr
    i64 front(Node* root) {
        pushdown(root);
        while (root->left) {
            root = root->left;
            pushdown(root);
        }
        return root->val;
    }

    // 取得 Treap 中的最大值
    // 使用前必須保證 root != nullptr
    i64 back(Node* root) {
        pushdown(root);
        while (root->right) {
            root = root->right;
            pushdown(root);
        }
        return root->val;
    }
};

void solve() {
    int n, l, r;
    cin >> n;

    FHQTreap tr(n);

    using Node = FHQTreap::Node;

    Node* f = nullptr;

    for (int i = 0; i < n; i++) {
        cin >> l >> r;

        // A: < l, B: >= l
        auto [A, B] = tr.split(f, l);
        // C: [l, r), D: >= r
        auto [C, D] = tr.split(B, r);

        // [l, r) 這段全部 +1
        C = tr.update(C, l, r, 1);  // 其實 tr.apply(C, 1) 就可以了

        // 刪掉第一個 >= r 的 DP 值
        D = tr.popmin(D);

        // 插入新的 l
        C = tr.insert(C, l);

        // 合併
        f = tr.merge(tr.merge(A, C), D);
    }

    cout << tr.size(f) << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}