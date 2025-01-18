#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

// Trie 用於取得字串的 index
class TrieNode {
public:
    unordered_map<int, TrieNode*> child; // 如果用 array 或 vector 會 MLE
    int idx;
    TrieNode() : idx(-1) {}
};

class Trie {
public:
    TrieNode* root;
    int cnt; // 保存的單字數量
    Trie() : root(new TrieNode()), cnt(0) {}

    int insert(const string& word) {
        TrieNode* node = root;
        for (char ch : word) {
            int idx = ch - 'a';
            if (node->child.find(idx) == node->child.end()) {
                node->child[idx] = new TrieNode();
            }
            node = node->child[idx];
        }
        if (node->idx == -1) {
            node->idx = cnt++;
        }
        return node->idx;
    }
};

// Disjoint Set Union 用於判斷圖是否連通
class UnionFind {
public:
    vector<int> pa, sz;
    int cnt;
    UnionFind(int n) : pa(n), sz(n, 1), cnt(n) {
        iota(pa.begin(), pa.end(), 0);
    }
    int find(int x) {
        if (pa[x] != x) {
            pa[x] = find(pa[x]);
        }
        return pa[x];
    }
    bool _union(int x, int y) {
        int px = find(x), py = find(y);
        if (px == py) return false;
        if (sz[px] > sz[py]) {
            swap(px, py);
        }
        pa[px] = py;
        sz[py] += sz[px];
        cnt--;
        return true;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    string s, t;
    vector<pair<int, int>> edges; // 保存邊
    Trie trie;
    while (cin >> s >> t) {
        int u = trie.insert(s);
        int v = trie.insert(t);
        edges.emplace_back(u, v);
    }
    
    // 取得節點數並合併節點
    int n = trie.cnt; // 節點數
    UnionFind uf(n); // 初始化 Disjoint Set Union
    vector<int> cnt(n, 0); // 保存每個節點的度數
    for (auto& [u, v] : edges) {
        uf._union(u, v); // 合併節點
        cnt[u]++;
        cnt[v]++;
    }
    
    // 直接用 DSU 的連通分量數 cnt 來判斷圖是否連通
    bool is_connected = (uf.cnt <= 1); // 如果節點個數為 0 時，則 uf.cnt 會是 0，所以要 <= 1
    
    // 判斷圖是否為歐拉圖
    int cnt_odd = 0;
    for (int i = 0; i < n; ++i) {
        if (cnt[i] % 2 == 1) {
            cnt_odd++;
        }
    }

    // 輸出結果
    cout << ((cnt_odd == 0 || cnt_odd == 2) && is_connected ? "Possible" : "Impossible") << endl;
    return 0;
}