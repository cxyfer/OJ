/*
Aho-Corasick Automaton (AC 自動機)

Problems:
- https://www.luogu.com.cn/problem/P3808
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
            int c = ch - 'a';
            if (node->child[c] == nullptr) {
                node->child[c] = new Node();
            }
            node = node->child[c];
        }
        node->cnt += 1;  // 累加，防止有相同的模式串
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
        node = node->child[idx];  // 由於是 Trie 圖，直接轉移即可

        // 沿著 fail 鏈向上搜集所有匹配的模式串
        Node* temp = node;
        while (temp != ac.root && temp->cnt != -1) {
            ans += temp->cnt;
            temp->cnt = -1;  // 標記為 -1，代表此節點已被統計過，避免重複計算
            temp = temp->fail;
        }
    }
    cout << ans << endl;
    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}