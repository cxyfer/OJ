#include <bits/stdc++.h>
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
    vector<Node*> pos, order;

    AhoCorasick() {
        root = new Node();
    }

    void insert(const string& word) {
        Node* node = root;
        for (char ch : word) {
            int idx = ch - 'a';
            if (node->child[idx] == nullptr)
                node->child[idx] = new Node();
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
                order.push_back(root->child[i]);
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
                    order.push_back(v);
                }
            }
        }
    }
};

void solve() {
    int n;
    cin >> n;
    vector<string> words(n);
    string t;
    for (auto & word : words) cin >> word;
    cin >> t;

    AhoCorasick ac;
    for (auto & word : words) ac.insert(word);
    ac.build();
    
    Node* node = ac.root;
    for (char ch : t) {
        int idx = ch - 'a';
        while (node != ac.root && node->child[idx] == nullptr) node = node->fail;
        if (node->child[idx] != nullptr) node = node->child[idx];
        node->cnt++;
    }

    reverse(ac.order.begin(), ac.order.end());
    for (auto & node : ac.order)
        node->fail->cnt += node->cnt;

    for (auto & node : ac.pos)
        cout << node->cnt << endl;
    return;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    solve();
    return 0;
}