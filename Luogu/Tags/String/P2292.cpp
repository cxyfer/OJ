/*
P2292 [HNOI2004] L 语言
https://www.luogu.com.cn/problem/P2292
AC自動機優化DP

f[i] 表示 target[..i] 的後綴能否被 words 中的字串覆蓋，若能覆蓋則 f[i] =
True，否則 f[i] = False。 f[i] = f[i - len(word)]，其中 word 是 words 中的字串

注意關鍵剪枝：
1. 當前需要長度至少為 i - ans 的模式串才能匹配，但不能超過 max_len
2. 在沿著 last 往上尋找的過程中，已經匹配 (f[i] == True) 就沒必要再往上找了
*/

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
        node->length = word.length();
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

void solve() {
    int n, q;
    cin >> n >> q;

    AhoCorasick ac;
    string pattern, t;
    int max_len = 0;
    for (int i = 0; i < n; ++i) {
        cin >> pattern;
        ac.insert(pattern);
        max_len = max(max_len, (int)pattern.length());
    }
    ac.build();

    while (q--) {
        cin >> t;
        int m = t.length();

        int ans = 0;
        vector<bool> f(m + 1, false);
        f[0] = true;

        Node* node = ac.root;
        for (int i = 1; i <= t.length(); ++i) {
            // 剪枝：當前需要長度至少為 i - ans 的模式串才能匹配，
            // 但這個長度不可能超過 max_len
            if (i - ans > max_len) break;

            node = node->child[t[i - 1] - 'a'];

            // 沒有任何字串的前綴與 t[..i] 的後綴匹配
            if (node == ac.root) break;

            // 沿著 last 往上尋找
            Node* temp = node;
            while (temp != ac.root) {
                f[i] = f[i] || f[i - temp->length];
                // 剪枝：已經匹配就沒必要再往上找了，主要是這個避免 TLE
                if (f[i]) {
                    ans = i;  // 更新答案
                    break;
                }
                temp = temp->last;
            }
        }
        cout << ans << endl;
    }
    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}