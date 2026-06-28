#include <bits/stdc++.h>
using namespace std;
const int ALPH = 26;
#define endl '\n'

struct Node {
    array<Node*, ALPH> child;
    Node *fail, *last;
    int length;
    Node() : fail(nullptr), last(nullptr), length(0) {
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
            int idx = ch - 'a';
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

    void build2() {
        root->fail = root->last = root;
        // BFS
        queue<Node*> q;
        for (int i = 0; i < ALPH; ++i) {
            if (root->child[i] != nullptr) {
                root->child[i]->fail = root->child[i]->last = root;
                q.push(root->child[i]);
            }
        }
        while (!q.empty()) {
            Node* u = q.front();
            q.pop();
            for (int i = 0; i < ALPH; ++i) {
                Node* v = u->child[i];
                if (v == nullptr) continue;
                Node* fu = u->fail;
                while (fu != root && fu->child[i] == nullptr) fu = fu->fail;
                v->fail = (fu->child[i] != nullptr) ? fu->child[i] : root;
                v->last = (v->fail->length > 0) ? v->fail : v->fail->last;
                q.push(v);
            }
        }
    }
};