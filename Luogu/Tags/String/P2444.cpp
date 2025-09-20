#include <bits/stdc++.h>
using namespace std;
const int ALPH = 2;
#define endl '\n'

struct Node {
    array<Node*, ALPH> child;
    Node *fail, *last;
    int length;
    bool vis, ins;
    Node() : fail(nullptr), last(nullptr), length(0), vis(false), ins(false) {
        fill(child.begin(), child.end(), nullptr);
    }
};

class AhoCorasick {
public:
    Node* root;
    vector<Node*> pos;

    AhoCorasick() {
        root = new Node();
    }

    void insert(const string& word) {
        Node* node = root;
        for (char ch : word) {
            int idx = ch - '0';
            if (node->child[idx] == nullptr) node->child[idx] = new Node();
            node = node->child[idx];
        }
        pos.push_back(node);
        node->length = word.length();
    }

    void build() {
        root->fail = root->last = root;
        // BFS
        queue<Node*> q;
        for (int i = 0; i < ALPH; ++i) {
            if (root->child[i] == nullptr) {
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
                if (u->child[i] == nullptr) {
                    u->child[i] = u->fail->child[i];
                } else {
                    Node* v = u->child[i];
                    v->fail = u->fail->child[i];
                    v->last = (v->fail->length > 0) ? v->fail : v->fail->last;
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
    AhoCorasick ac;
    for (auto& word : words) {
        cin >> word;
        ac.insert(word);
    }
    ac.build();

    auto dfs = [&](this auto&& dfs, Node* u) -> bool {
        u->vis = u->ins = true;
        for (int i = 0; i < ALPH; ++i) {
            Node* v = u->child[i];
            if (v == nullptr) continue;
            if (v->length > 0 || v->last != ac.root) continue;
            if (!v->vis) {
                if (dfs(v)) return true;
            } else if (v->ins) {
                return true;
            }
        }
        u->ins = false;
        return false;
    };
    cout << (dfs(ac.root) ? "TAK" : "NIE") << endl;
    return;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    solve();
    return 0;
}