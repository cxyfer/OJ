/*
 * @lc app=leetcode id=3213 lang=cpp
 *
 * [3213] Construct String with Minimum Cost
 */

// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
#include <bits/stdc++.h>
using namespace std;
const int ALPH = 26;
#define endl '\n'

struct Node {
    array<Node*, ALPH> child;
    Node *fail, *last;
    int length, cost;
    Node() : fail(nullptr), last(nullptr), length(0), cost(INT_MAX) {
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

    void insert(const string& word, int cost) {
        Node* node = root;
        for (char ch : word) {
            int idx = ch - 'a';
            if (node->child[idx] == nullptr) node->child[idx] = new Node();
            node = node->child[idx];
        }
        pos.push_back(node);
        node->length = word.length();
        node->cost = min(node->cost, cost);
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

class Solution1 {
public:
    int minimumCost(string target, vector<string>& words, vector<int>& costs) {
        AhoCorasick ac = AhoCorasick();
        for (auto [word, cost] : ranges::views::zip(words, costs)) {
            ac.insert(word, cost);
        }
        ac.build();

        int n = target.length();
        vector<int> f(n + 1, INT_MAX / 2);
        f[0] = 0;
        Node* node = ac.root;
        for (int i = 1; i <= n; ++i) {
            int c = target[i - 1] - 'a';
            node = node->child[c];
            if (node->length > 0) {  // 匹配到了一個盡可能長的 words[k]
                f[i] = min(f[i], f[i - node->length] + node->cost);
            }
            // 沿著 last 往上尋找，可能可以找到其餘更短，但可以使成本更小的 words[k]
            Node* temp = node->last;
            while (temp != ac.root) {
                f[i] = min(f[i], f[i - temp->length] + temp->cost);
                temp = temp->last;
            }
        }
        return f[n] < INT_MAX / 2 ? f[n] : -1;
    }
};

class Solution2 {
public:
    int minimumCost(string target, vector<string>& words, vector<int>& costs) {
        int n = target.length();
        const int MOD = 1'070'777'777;
        mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
        const int BASE = uniform_int_distribution<>(8e8, 9e8)(rng);
        vector<long long> P(n + 1), H(n + 1);
        P[0] = 1;
        for (int i = 0; i < n; i++) {
            P[i + 1] = P[i] * BASE % MOD;
            H[i + 1] = (H[i] * BASE + target[i]) % MOD;
        }

        map<int, unordered_map<long long, int>> min_cost; // 长度 -> 哈希值 -> 最小成本
        for (int i = 0; i < words.size(); i++) {
            long long h1 = 0, h2 = 0;
            long long h = 0;
            for (char b : words[i]) {
                h = (h * BASE + b) % MOD;
            }
            int ln = words[i].length();
            if (!min_cost[ln].contains(h)) {
                min_cost[ln][h] = costs[i];
            } else {
                min_cost[ln][h] = min(min_cost[ln][h], costs[i]);
            }
        }

        vector<int> f(n + 1, INT_MAX / 2);
        f[0] = 0;
        for (int i = 1; i <= n; i++) {
            for (auto& [ln, mc] : min_cost) {
                if (ln > i) {
                    break;
                }
                long long h = ((H[i] - H[i - ln] * P[ln]) % MOD + MOD) % MOD;
                auto it = mc.find(h);
                if (it != mc.end()) {
                    f[i] = min(f[i], f[i - ln] + it->second);
                }
            }
        }
        return f[n] == INT_MAX / 2 ? -1 : f[n];
    }
};

using Solution = Solution1;
// using Solution = Solution2;
// @lc code=end
