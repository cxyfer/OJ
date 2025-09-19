/*
P3808 AC 自动机（简单版）
https://www.luogu.com.cn/problem/P3808
*/
#include <bits/stdc++.h>
using namespace std;
constexpr int ALPH = 26;
#define endl '\n'

struct Node {
    array<Node*, ALPH> child;
    Node* fail;
    int cnt;
    Node() : fail(nullptr), cnt(0) {
        fill(child.begin(), child.end(), nullptr);
    }
};

class AhoCorasick {
public:
    Node* root;

    AhoCorasick() {
        root = new Node();
    }

    void insert(const string& word) {
        Node* node = root;
        for (char ch : word) {
            int idx = ch - 'a';
            if (node->child[idx] == nullptr) node->child[idx] = new Node();
            node = node->child[idx];
        }
        node->cnt += 1;
    }

    void build() {
        root->fail = root;
        // BFS
        queue<Node*> q;
        for (int i = 0; i < ALPH; ++i) {
            if (root->child[i] == nullptr) {
                root->child[i] = root;
            } else {
                root->child[i]->fail = root;
                q.push(root->child[i]);
            }
        }
        while (!q.empty()) {
            Node* u = q.front();
            q.pop();
            for (int i = 0; i < ALPH; ++i) {
                if (u->child[i] == nullptr) {
                    u->child[i] = u->fail->child[i];
                } else {
                    Node* v = u->child[i];
                    v->fail = u->fail->child[i];
                    q.push(v);
                }
            }
        }
    }
};

void solve() {
    int n;
    cin >> n;
    vector<string> words(n);
    for (int i = 0; i < n; ++i) cin >> words[i];
    string t;
    cin >> t;

    AhoCorasick ac;
    for (const auto& word : words) ac.insert(word);
    ac.build();

    int ans = 0;
    Node* node = ac.root;
    for (char ch : t) {
        int idx = ch - 'a';
        while (node != ac.root && node->child[idx] == nullptr)
            node = node->fail;
        if (node->child[idx] != nullptr) node = node->child[idx];
        if (node->cnt > 0) {
            ans += node->cnt;
            node->cnt = 0;
        }
    }
    cout << ans << endl;
    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}