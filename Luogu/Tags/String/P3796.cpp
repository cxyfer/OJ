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
};

void solve(int n) {
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
        Node* v = node;
        while (v != ac.root) {
            v->cnt += 1;
            v = v->last;
        }
    }

    int mx = 0;
    vector<string> ans;
    for (int i = 0; i < n; ++i) {
        Node* node = ac.pos[i];
        string word = words[i];
        if (node->cnt > mx) {
            mx = node->cnt;
            ans = {word};
        } else if (node->cnt == mx) {
            ans.push_back(word);
        }
    }
    cout << mx << endl;
    for (auto & word : ans) cout << word << endl;
    return;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n;
    while (cin >> n && n) solve(n);
    return 0;
}