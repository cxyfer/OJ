#include <bits/stdc++.h>
using namespace std;
using i64 = long long;
const int MAX_CHARS = 2 * 1024 * 1024 + 10;
#define endl '\n'

template <typename T = char>
class FHQTreap {
public:
    class Node {
    public:
        Node *left, *right;
        int sz;
        uint32_t pri;
        T val;

        Node(T val, uint32_t pri)
            : left(nullptr), right(nullptr), sz(1), pri(pri), val(val) {}
    };

private:
    vector<Node> pool;
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

    Node* make(T value) {
        pool.emplace_back(value, rng());
        return &pool.back();
    }

    void pushup(Node* root) {
        if (!root) return;
        root->sz = size(root->left) + size(root->right) + 1;
    }

    /*
        split(root, k)

        將 root 代表的序列切成 a, b 兩棵 Treap：

        a：前 k 個字元
        b：剩下的字元
    */
    pair<Node*, Node*> split(Node* root, int k) {
        if (!root) return {nullptr, nullptr};
        if (k <= size(root->left)) {
            auto [a, b] = split(root->left, k);
            root->left = b;
            pushup(root);
            return {a, root};
        } else {
            auto [a, b] = split(root->right, k - size(root->left) - 1);
            root->right = a;
            pushup(root);
            return {root, b};
        }
    }

    /*
        merge(a, b)

        將兩段序列接起來。

        使用前只需要保證：
        a 這段文字在 b 前面。
    */
    Node* merge(Node* a, Node* b) {
        if (!a || !b) return a ? a : b;

        if (a->pri < b->pri) {
            a->right = merge(a->right, b);
            pushup(a);
            return a;
        } else {
            b->left = merge(a, b->left);
            pushup(b);
            return b;
        }
    }

private:
    /*
        重新計算整棵子樹大小。
        build 時使用。
    */
    int rebuildSize(Node* root) {
        if (!root) return 0;
        root->sz = rebuildSize(root->left) + rebuildSize(root->right) + 1;
        return root->sz;
    }

public:
    /*
        用一個字串建立一棵 Treap。

        這裡使用單調棧做 O(n) 建樹，
        比逐字 merge 的 O(n log n) 更快。
    */
    Node* build(const string& s) {
        if (s.empty()) return nullptr;

        vector<Node*> stk;
        stk.reserve(s.size());

        Node* root = nullptr;

        for (char c : s) {
            Node* cur = make(c);
            Node* last = nullptr;

            while (!stk.empty() && stk.back()->pri > cur->pri) {
                last = stk.back();
                stk.pop_back();
            }

            cur->left = last;

            if (!stk.empty()) {
                stk.back()->right = cur;
            } else {
                root = cur;
            }

            stk.push_back(cur);
        }

        rebuildSize(root);
        return root;
    }

    /*
        中序遍歷，把一段 Treap 轉成字串。
    */
    string collect(Node* root) {
        if (!root) return "";
        return collect(root->left) + static_cast<char>(root->val) + collect(root->right);
    }

    /*
        在 pos 位置插入字串 s。

        pos 表示游標前面有幾個字元。
    */
    void insert(Node*& root, int pos, const string& s) {
        auto [A, B] = split(root, pos);
        Node* mid = build(s);
        root = merge(merge(A, mid), B);
    }

    /*
        刪除 pos 後面的 len 個字元。
    */
    void erase(Node*& root, int pos, int len) {
        auto [A, B] = split(root, pos);
        auto [C, D] = split(B, len);
        root = merge(A, D);
    }

    /*
        取得 pos 後面的 len 個字元，輸出到 out。
        Treap 結構最後會還原。
    */
    string get(Node*& root, int pos, int len) {
        auto [A, B] = split(root, pos);
        auto [C, D] = split(B, len);
        string res = collect(C);
        root = merge(A, merge(C, D));
        return res;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    FHQTreap<char> tr(MAX_CHARS);

    using Node = FHQTreap<char>::Node;

    Node* root = nullptr;
    int cursor = 0;  // cursor 表示游標前方有幾個字元。

    string op, s;
    int k, n;
    while (t--) {
        cin >> op;
        if (op[0] == 'M') {  // Move
            cin >> cursor;
        } else if (op[0] == 'I') {  // Insert
            cin >> n;
            s.clear();
            s.reserve(n);

            char ch;
            /*
                讀完 n 之後，後面會有一個分隔字元。
                通常是換行，也可能是空格。
                這個分隔字元不是插入內容的一部分，所以先吃掉。
            */
            cin.get(ch);
            /*
                題目說 Insert 的字串中可能插入一些回車符，要忽略它們。
                這裡同時忽略 '\n' 和 '\r'
            */
            while ((int)s.size() < n && cin.get(ch)) {
                if (ch == '\n' || ch == '\r') continue;
                s.push_back(ch);
            }

            tr.insert(root, cursor, s);
        } else if (op[0] == 'D') {  // Delete
            cin >> n;
            tr.erase(root, cursor, n);
        } else if (op[0] == 'G') {  // Get
            cin >> n;
            cout << tr.get(root, cursor, n) << endl;
        } else if (op[0] == 'P') {  // Prev
            cursor--;
        } else if (op[0] == 'N') {  // Next
            cursor++;
        }
    }
    return 0;
}