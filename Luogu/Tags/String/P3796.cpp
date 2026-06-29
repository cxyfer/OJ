#include <bits/stdc++.h>

#include <ranges>

using namespace std;
const int ALPH = 26;
#define endl '\n'

struct Node {
    array<Node*, ALPH> child;
    Node *fail, *last;
    int length, cnt;
    Node() : fail(nullptr), last(nullptr), length(0), cnt(0) {
        fill(child.begin(), child.end(), nullptr);
    }
};

class AhoCorasick {
public:
    Node* root;

    AhoCorasick() {
        root = new Node();
    }

    Node* insert(const string& word) {
        Node* node = root;
        for (char ch : word) {
            int idx = ch - 'a';
            if (node->child[idx] == nullptr) node->child[idx] = new Node();
            node = node->child[idx];
        }
        node->length = word.length();
        return node;
    }

    void build() {
        root->fail = root->last = root;
        // BFS
        queue<Node*> q;
        for (int i = 0; i < ALPH; ++i) {
            if (root->child[i] == nullptr) {
                // 添加虛擬子節點
                root->child[i] = root;
            } else {
                root->child[i]->fail = root->child[i]->last = root;
                q.push(root->child[i]);
            }
        }
        while (!q.empty()) {
            Node* u = q.front();
            q.pop();
            for (int i = 0; i < ALPH; ++i) {
                Node* v = u->child[i];
                if (v == nullptr) {
                    // 添加虛擬子節點
                    u->child[i] = u->fail->child[i];
                } else {
                    // 失配位置
                    v->fail = u->fail->child[i];
                    // 上一個一定是某個 word 結尾的節點
                    v->last = (v->fail->length > 0) ? v->fail : v->fail->last;
                    q.push(v);
                }
            }
        }
    }
};

void solve(int n) {
    vector<string> words(n);
    string t;
    for (auto& word : words) cin >> word;
    cin >> t;

    AhoCorasick ac;
    vector<Node*> nodes;
    for (auto& word : words) nodes.push_back(ac.insert(word));
    ac.build();

    Node* node = ac.root;
    for (char ch : t) {
        node = node->child[ch - 'a'];

        // 沿著 last 鏈向上搜集所有匹配的模式串
        Node* temp = node;
        while (temp != ac.root) {
            temp->cnt += 1;
            temp = temp->last;
        }
    }

    int mx = 0;
    vector<string> ans;
    for (auto&& [node, word] : views::zip(nodes, words)) {
        if (node->cnt > mx) {
            mx = node->cnt;
            ans = {word};
        } else if (node->cnt == mx) {
            ans.push_back(word);
        }
    }
    cout << mx << endl;
    for (auto& word : ans) cout << word << endl;
    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    while (cin >> n && n) solve(n);
    return 0;
}