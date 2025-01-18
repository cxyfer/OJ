#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const LL MOD = 1e9 + 7;
#define endl '\n'

class TrieNode {
public:
    TrieNode* child[26];
    bool is_end;
    TrieNode() {
        memset(child, 0, sizeof(child));
        is_end = false;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, k;
    string s, word;
    cin >> s;
    n = s.size();
    cin >> k;
    TrieNode* root = new TrieNode();
    while (k--) {
        cin >> word;
        TrieNode* node = root;
        for (char ch : word) {
            int idx = ch - 'a';
            if (node->child[idx] == nullptr) {
                node->child[idx] = new TrieNode();
            }
            node = node->child[idx];
        }
        node->is_end = true;
    }
    vector<LL> f(n + 1);
    f[n] = 1;
    for (int i = n - 1; i >= 0; --i) {
        TrieNode* node = root;
        for (int j = i; j < n; ++j) {
            int idx = s[j] - 'a';
            if (node->child[idx] == nullptr) break;
            node = node->child[idx];
            if (node->is_end) {
                f[i] = (f[i] + f[j + 1]) % MOD;
            }
        }
    }
    cout << f[0] << endl;
    return 0;
}